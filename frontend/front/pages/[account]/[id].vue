<template>
    <div>
        <h1>{{ title }}</h1>
        <img :src="`${endpoint}image/${imagefilename}`" alt="" class="image">
        <router-link class="profile" :to="`/${username}`">
            <div class="icon"></div>
            <span>{{ username }}</span>
        </router-link>
        <div class="content">
            <p>{{ description }}</p>
        </div>
        <div class="bottom">

            <img v-if="isKeeped" src="assets/keep2.png" alt="keep">
            <img v-else src="assets/keep1.png" alt="keep" @click="Keep">

        </div>
    </div>
</template>

<script>
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            title: '',
            fork: null,
            username: null,
            description: '',
            imagefaile: null,
            endpoint: endpoint,
            isKeeped: false,
        }
    },
    methods : {
        async Keep() {
            try {
                const response = await fetch(endpoint + `keep?idea_id=${this.$route.params.id}`,
                    {
                        method: 'GET',
                        credentials: 'include',
                    }
                );
                const data = await response.json();
                console.log(data);
                this.isKeeped = true;
            } catch (error) {
                console.error('Error:', error);
            }
        }   
    },
    async created() {
        const response = await fetch(endpoint + `idea/${this.$route.params.id}`);
        const data = await response.json();
        this.title = data.idea.title;
        this.username = data.username;
        this.description = data.idea.description;
        this.imagefilename = data.idea.image;
        try {
            const response = await fetch(endpoint + `user/keep/${this.$route.params.id}`,
                {
                    method: 'GET',
                    credentials: 'include',
                }
            );
            const data = await response.json();
            console.log(data);
            if (data.result === "Success") {
                this.isKeeped = true;
            }
                

        } catch (error) {
            console.error('Error:', error);
        }
    },
    async getKeep() {
        try {
            const response = await getch(endpoint + `idea/user/keep/${this.$route.params.id}`,
                {
                    method: 'GET',
                    credentials: 'include',
                }
            );
            const data = await response.json();
            console.log(data);

        } catch (error) {
            console.error('Error:', error);
        }
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New&display=swap');

.content {
    display: flex;
    flex-direction: column;
    margin: 25px;
    margin-bottom: 140px;
}

h1 {
    font-family: "Zen Kaku Gothic New", sans-serif;
    font-size: 30px;
    font-weight: bold;
    padding: 20px 0;
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 20px;
}

p {
    font-family: "Zen Kaku Gothic New", sans-serif;
    font-size: 16px;
    line-height: 1.5;
}

.bottom {
    border-top: 1px solid #a2a2a2;
    background-color: #fff;
    display: flex;
    position: fixed;
    margin-top: 20px;
    bottom: 60px;
    width: 100%;
    padding-top: 10px;
    padding-bottom: 15px;
    justify-content: space-around;
}

.bottom img {
    width: 30px;
    height: 30px;
    display: block;
}

.image {
    width: 85%;
    height: auto;
    margin: 0 auto;
    display: block;
    border-radius: 5px;
    margin-bottom: 5px;
}

.profile {
    font-family: "Zen Kaku Gothic New", sans-serif;
    display: flex;
    align-items: center;
    padding: 10px 40px;
    border-bottom: 1px solid #ddd;
    text-decoration: none;
    color: #000;
}

.icon {
    width: 40px;
    height: 40px;
    background-color: black;
    border-radius: 50%;
    margin-right: 10px;
}
</style>