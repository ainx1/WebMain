from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    class Role(models.IntegerChoices):
        undefined = 0, ("Не определена")
        customer = 1, ("Покупатель")
        manager = 2, ("Менеджер")

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    role = models.SmallIntegerField("Роль пользователя", choices=Role, default=Role.undefined)
    phone = models.TextField("Номер телефона", null=True, blank=True)
    address = models.TextField("Адрес доставки", null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else f"Profile {self.id}"

@receiver(post_save, sender=User)
def on_user_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)



# 1) категория
class Category(models.Model):
    name = models.TextField("Название категории")
    image = models.ImageField("Картинка", null=True, blank=True, upload_to="category_images")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name

# 2) производитель
class Manufacturer(models.Model):
    name = models.TextField("Название производителя")
    country = models.TextField("Страна", null=True, blank=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self) -> str:
        return self.name

# 3) комплектующее
class Component(models.Model):
    name = models.TextField("Наименование комплектующего")
    category = models.ForeignKey("PCShop.Category", on_delete=models.CASCADE, null=True, verbose_name="Категория")
    manufacturer = models.ForeignKey("PCShop.Manufacturer", on_delete=models.CASCADE, null=True, verbose_name="Производитель")
    price = models.IntegerField("Цена", null=True)
    stock = models.SmallIntegerField("Остаток на складе", null=True)
    description = models.TextField("Описание", null=True, blank=True)
    image = models.ImageField("Картинка", null=True, blank=True, upload_to="component_images")

    class Meta:
        verbose_name = "Комплектующее"
        verbose_name_plural = "Комплектующие"

    def __str__(self) -> str:
        return self.name

# 4) заказ (бизнес-процесс покупки)
class Order(models.Model):
    customer_name = models.TextField("ФИО покупателя")
    customer_phone = models.TextField("Номер телефона", null=True)
    customer = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, verbose_name="Покупатель")
    status = models.TextField("Статус заказа", null=True)
    date = models.DateField("Дата заказа", null=True)
    time = models.TimeField("Время заказа", null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return f"Заказ №{self.id} — {self.customer_name}"

# 5) товар в заказе (связь между заказом и комплектующим)
class OrderItem(models.Model):
    order = models.ForeignKey("PCShop.Order", on_delete=models.CASCADE, null=True, verbose_name="Заказ")
    product = models.ForeignKey("PCShop.Component", on_delete=models.CASCADE, null=True, verbose_name="Комплектующее")
    quantity = models.SmallIntegerField("Количество", null=True)
    price = models.IntegerField("Цена при покупке", null=True)

    class Meta:
        verbose_name = "Комплектующее в заказе"
        verbose_name_plural = "Комплектующие в заказе"

    def __str__(self) -> str:
        return f"{self.product} (x{self.quantity})"


class PcBuild(models.Model):
    name = models.TextField("Название сборки")
    product = models.ManyToManyField("PCShop.Component", blank=True, verbose_name="Комплектующие в сборке")
    image = models.ImageField("Картинка сборки", null=True, blank=True, upload_to="pc_build_images")

    class Meta:
        verbose_name = "Шаблон сборки ПК"
        verbose_name_plural = "Шаблоны сборок ПК"

    def __str__(self) -> str:
        return self.name