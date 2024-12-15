<template>
    <div>
        <a href="/home">
            <img v-if="home" src="@/assets/home.png" alt="home" />
            <img v-else src="@/assets/home2.png" alt="home" />
        </a>
        <a href="/palette">
            <img v-if="palette" src="@/assets/folder.png" alt="folder" />
            <img v-else src="@/assets/folder2.png" alt="folder" />
        </a>
        <a href="/search">
            <img v-if="search" src="@/assets/search.png" alt="search" />
            <img v-else src="@/assets/search2.png" alt="search" />
        </a>
        <a :href="islogin ? '/' + me : '/login'">
            <img v-if="human" src="@/assets/human.png" alt="human" />
            <img v-else src="@/assets/human2.png" alt="human" />
        </a>
    </div>
</template>

<script>
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            me : '',
            islogin: false,
            home: false,
            palette: false,
            search: false,
            brain: false,
            human: false
        }
    },
    methods: {
        async fetchData() {
            const response = await fetch(endpoint + 'me',
                {
                    credentials: 'include'
                }
            );
            const data = await response.json();
                this.me = data.username;
            if(data.detail==="Success"){
                this.islogin = true;
            }

            if (this.$route.path === '/home') {
                this.home = true
            } else if (this.$route.path === '/palette') {
                this.palette = true
            } else if (this.$route.path === '/search') {
                this.search = true
            } else if (this.$route.path === '/brain') {
                this.brain = true
            } else if (this.$route.path === '/' + this.me) {
                this.human = true
            }
        }
    },
    created() {
        this.fetchData();
    },
}
</script>

<style scoped>
div {
    display: flex;
    background-color: #fff;
    border-top: 1px solid #A2A2A2;
    justify-content: space-around;
    padding: 15px 30px 15px 30px;
    position: fixed;
    bottom: 0px;
    width: 85%;
    z-index: 10;
}

img {
    width: 30px;
    height: 30px;
}
</style>