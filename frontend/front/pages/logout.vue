<template>
    <div>
        <h1>ログアウト</h1>
        <input type="button" @click="logout" value="ログアウト">
    </div>
</template>

<script>
import { endpoint } from '~/components/APIEndPoint';
export default {

    methods: {
        async logout() {
            const response = await fetch(endpoint+'logout', {
                method: 'POST',
                credentials: 'include'
            });
            if (response.ok) {
              console.log('Logout success');
                this.$router.push('/login');
            } else {
                console.error('Logout failed');
            }
        }
    }
}
</script>