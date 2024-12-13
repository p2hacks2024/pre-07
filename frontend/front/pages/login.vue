<template>
    <div>
        <form @submit.prevent="login">
            <div>
                <label for="username">Username:</label>
                <input type="text" v-model="username" id="username" required>
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" v-model="password" id="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
import { endpoint } from '~/components/APIEndPoint';
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        async login() {
            try {
                const formData = new FormData();
                formData.append('username', this.username);
                formData.append('password', this.password);

                const response = await fetch(endpoint + 'login', {
                    method: 'POST',
                    body: formData
                });
                if (response.ok) {
                    this.$router.push('/home');
                } else {
                    const errorData = await response.json();
                    console.error('Login failed', errorData.detail || response.statusText);
                }
            } catch (error) {
                console.error('Login failed', error);
            }
        }
    }
};
</script>