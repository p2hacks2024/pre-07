<template>
    <router-link :href="`/test/${id}`">
        <div class="postView">
            <img src="https://s3-alpha-sig.figma.com/img/24d4/9623/89e7d20455cd946da2c7a04f25e0b53e?Expires=1734912000&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=aB4zDlEK-PNKzH6d9HGm2fIezFDgx4cPReh5sUFllWYTj5aEEwsGbBug5DB~nlEZ3Maz9FmV-eHPCcUyT2xi48X3uA3HrE2Oso4BOGorQxu6nWfxwNyR-5OgWG0eYToQ-M4RqfI8LwQPe77gDWGhVqkv5JuxTcUcIV-qZxWgY7yicXD32sbgF7FKLqHEUI2hP-oWuDZhvbg-Zzl7L1udJfbl0eWXoXxQidnVMuLIzrWSY8zOskyUIhyrvopS3uRcqj9B4EHXSexJg1V3P~cUyyEDFB-co-QN0wL~e3iMUexqrnK1zK9nw-ZWeMwYjxsJHd6wzTJkgmrekYhzvlQICA__">
            <div class="contents">
                <h1>{{ title }}</h1>
                <p>{{ description }}</p>
            </div>
            <div class="account">
                <div class="icon"></div>
                <p>{{ username }}</p>
            </div>
        
        </div>
    </router-link>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New&display=swap');
    .postView {
        border-radius: 15px;
        background-color: #fff;
        color: black;
        text-decoration: none;
        margin: 5%;
    }
    img {
        border-radius: 15px 15px 0 0;
        width: 100%;
        height: 100%;
    }
    h1 {
        font-family: "Zen Kaku Gothic New", sans-serif;
        margin: 0;
        padding: 0;
        font-size: 20px;
    }
    p {
        font-family: "Zen Kaku Gothic New", sans-serif;
        margin: 0;
        padding: 0;
    }
    .contents {
        padding: 5px;
    }
    .account {
        border-top: 1px solid #bdbdbd;
        padding: 5px;
        display: flex;
    }
    .icon p {
        display: table-cell;
        text-align: center;
        vertical-align: middle;
    }
    .icon {
        border-radius: 50%;
        height: 20px;
        width: 20px;
        background-color: black;
        margin-right: 5px;
    }
</style>

<script>
export default {
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            title: '',
            description: '',
            username: '' // 初期値を設定
        }
    },
    async created() {
        const response = await fetch(`http://10.124.75.43:8000/api/ideas/${this.id}`)
        const data = await response.json()
        this.title = data.idea.title
        this.description = data.idea.description
        this.user_id = data.idea.user_id
        
        const user_response = await fetch(`http://10.124.75.43:8000/api/user/${this.user_id}`)
        const user_data = await user_response.json()
        this.username = user_data.name
    },
}

</script>