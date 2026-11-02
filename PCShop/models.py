from django.db import models


class Category(models.Model):
    name = models.TextField("Название категории")
    image = models.ImageField("Картинка", null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Manufacturer(models.Model):
    name = models.TextField("Название производителя")
    country = models.TextField("Страна", null=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.TextField("Наименование товара")
    category = models.ForeignKey("PCShop.Category", on_delete=models.CASCADE, null=True, verbose_name="Категория")
    manufacturer = models.ForeignKey("PCShop.Manufacturer", on_delete=models.CASCADE, null=True, verbose_name="Производитель")
    price = models.IntegerField("Цена", null=True)
    stock = models.SmallIntegerField("Остаток на складе", null=True)
    image = models.ImageField("Картинка", null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer_name = models.TextField("ФИО покупателя")
    customer_phone = models.TextField("Номер телефона", null=True)
    status = models.TextField("Статус заказа", null=True)
    date = models.DateField("Дата заказа", null=True)
    time = models.TimeField("Время заказа", null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return f"Заказ №{self.id} — {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey("PCShop.Order", on_delete=models.CASCADE, null=True, verbose_name="Заказ")
    product = models.ForeignKey("PCShop.Product", on_delete=models.CASCADE, null=True, verbose_name="Товар")
    quantity = models.SmallIntegerField("Количество", null=True)
    price = models.IntegerField("Цена при покупке", null=True)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def __str__(self) -> str:
        return f"{self.product} (x{self.quantity})"


class PcBuild(models.Model):
    name = models.TextField("Название сборки")
    product = models.ManyToManyField("PCShop.Product", null=True, verbose_name="Товары в сборке")
    image = models.ImageField("Картинка сборки", null=True, blank=True)

    class Meta:
        verbose_name = "Шаблон сборки ПК"
        verbose_name_plural = "Шаблоны сборок ПК"

    def __str__(self) -> str:
        return self.name