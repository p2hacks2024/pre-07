<template>
    <div class="container">
        <div class="form-container">
            <h1>閃きをここで始めよう。</h1>
            <p>アカウントをお持ちですか？<a href="login"> ログイン</a></p>
            <div>
                <form @submit.prevent="signup">
                    <div class="input-group">
                        <label for="username">ユーザーネーム</label>
                        <input type="text" v-model="username" id="username" placeholder="user name" required>
                    </div>
                    <div>
                        <p v-if="invalidName" class="Error">すでに使われているユーザーネームです。</p>
                    </div>
                    <div class="input-group">
                        <label for="password">パスワード</label>
                        <input type="password" v-model="password" id="password" placeholder="password" required>
                    </div>
                    <div class="input-group">
                        <label for="password">パスワード (確認)</label>
                        <input type="password" v-model="passwordCheck" id="passwordCheck" placeholder="password (check)" required>
                    </div>
                    <div>
                        <p v-if="signupError" class="Error">パスワードが間違っています。もう一度入力してください。</p>
                    </div>
                    <div class="button-container">
                        <button type="submit" class="submit-button">登録</button>
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
            //form
            username: '',
            password: '',
            passwordCheck: '',
            //error
            signupError: false,
            invalidName: false,
        };
    },
    methods: {
        async signup() {
            if (this.password !== this.passwordCheck) {
                this.signupError = true;
                return;
            }

            try {
                const formData = new FormData();
                formData.append('username', this.username);
                formData.append('password', this.password);

                const response = await fetch(endpoint + 'signup', {
                    method: 'POST',
                    body: formData,
                    credentials: 'include'
                });
                if (response.ok) {
                    this.$router.push('/login');
                }else{
                    const errorData = await response.json();
                    if(errorData.detail === "Username already exists"){
                        this.invalidName = true;
                    }
                }
            } catch (error) {
                console.error('signup failed', error);
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

.Error {
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