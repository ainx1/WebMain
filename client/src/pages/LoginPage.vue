<script setup>
import useProfileStore from '@/stores/profileStore';
import { storeToRefs } from 'pinia';
import {ref} from 'vue';


const profileStore = useProfileStore();
const {
    isAuthenticated,
    userName
} = storeToRefs(profileStore)

const username = ref("")
const password = ref("")

async function onLoginClick() {
    profileStore.login(username.value, password.value)

}

</script>

<template>
    <div class="d-flex justify-content-center p-4">
        <form style="width: 350px" @submit.prevent.stop="onLoginClick">
            <div class="mb-3">
                <label class="form-label">Логин</label>
                <input v-model="username" required type="text" class="form-control">
            </div>
            <div class="mb-3">
                <label class="form-label">Пароль</label>
                <input v-model="password" required type="password" class="form-control">
            </div>
            <button class="btn btn-primary">Войти</button>
        </form>
    </div>
</template>

<style>
</style>