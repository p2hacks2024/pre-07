<template>
    <div class="container">
        <div class="form-container">
            <h1>閃きをここで始めよう。</h1>
            <p>アカウントをお持ちでない場合<a href="signup"> 登録</a></p>
            <div>
                <form @submit.prevent="login">
                    <div class="input-group">
                        <label for="username">ユーザーネーム</label>
                        <input type="text" v-model="username" id="username" placeholder="user name" required>
                    </div>
                    <div class="input-group">
                        <label for="password">パスワード</label>
                        <input type="password" v-model="password" id="password" placeholder="password" required>
                    </div>
                    <div>
                        <p v-if="loginError" class="loginError">ユーザーネーム、もしくはパスワードが間違っています。</p>
                    </div>
                    <div class="button-container">
                        <button type="submit" class="submit-button">ログイン</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { endpoint } from '~/components/APIEndPoint';
export default {
    data() {
        return {
            username: '',
            password: '',
            loginError: false,
        };
    },
    methods: {
        async login() {
            try {
                const formData = new FormData();
                formData.append('username', this.username);
                formData.append('password', this.password);

                const response = await fetch(endpoint + 'login', {
                    headers: {
                        'Content-Type': 'application/json',
                        'cookie': document.cookie
                    },
                    method: 'POST',
                    body: formData,
                    credentials: 'include'
                });
                if (response.ok) {
                    this.$router.push('/home');
                } else {
                    const errorData = await response.json();
                    console.error('Login failed', errorData.detail || response.statusText);
                    this.loginError = true;
                }
            } catch (error) {
                console.error('Login failed', error);
            }
        }
    }
};
</script>

<style scoped>

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.form-container {
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 300px;
}

h1 {
    font-size: 20px;
    margin-bottom: 5px;
}

p {
    font-size: 12px;
    margin-bottom: 20px;
}

p a {
    color: #007bff;
    text-decoration: none;
}

p a:hover {
    text-decoration: underline;
}

.loginError {
    color: red;
    margin-bottom: 10px;
    font-size: 10px;
}

.input-group {
    margin-bottom: 15px;
    text-align: left;
}

.input-group label {
    display: block;
    font-size: 14px;
    margin-bottom: 5px;
}

.input-group input {
    width: 100%;
    padding: 15px 30px;
    font-size: 14px;
    border: 1px solid #ccc;
    background-color: #D9D9D9;
    border-radius: 15px;
    box-sizing: border-box;
    text-align: center;
    color: #000000;
}

.button-container {
    margin-top: 100px;
}

.submit-button {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    color: #000;
    background-color: #ffeb3b;
    border: none;
    border-radius: 15px;
    cursor: pointer;
}

.submit-button:hover {
    background-color: #fdd835;
}
</style>