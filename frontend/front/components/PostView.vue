<template>
    <a :href="`/test/${id}`">
        <div class="postView">
            <img v-if="imagefilename" :src="`${endpoint}image/${imagefilename}`">
            <div class="contents">
                <h1>{{ title }}</h1>
                <p>{{ truncatedDescription }}</p>
            </div>
            <div class="account">
                <div class="icon" :style="iconStyle">
                    <span class="icon-text">{{ username ? username.charAt(0) : '' }}</span>
                </div>
                <p>{{ username }}</p>
            </div>

        </div>
    </a>
</template>
<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New&display=swap');
/* font-family: "Zen Kaku Gothic New", sans-serif; */
a {
    text-decoration: none;
    color: black;
}
img {
    width: 100%;
    max-height: 100px;
    object-fit: cover;
    border-radius: 20px 20px 0px 0px;
}
.postView {
    background-color: #f5f5f5;
    border-radius: 20px;
}
h1 {
    margin: 0px;
    padding: 0px;
    font-size: 140%;
}
.contents {
    padding-top: 5px;
    text-align: center;
    font-family: "Zen Kaku Gothic New", sans-serif;
    padding-left: 30px;
    padding-right: 30px;
}
.contents p {
    margin: 0px;
}
.account {
    font-family: "Zen Kaku Gothic New", sans-serif;
    padding: 3px 30px 10px 30px;
    border-top: 1px solid #dcdcdc;
    margin-top: 5px;
    display: flex;
    align-items: center;
}
.account p {
    margin: 0px;
    margin-left: 10px;
}

.icon {
    width: 40px;
    height: 40px;
    background-size: cover;
    background-position: center;
    border-radius: 50%;
    margin-right: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
    font-size: 20px;
}
.icon-text {
    font-size: 16px;
    color: white;
}
</style>

<script>
import{endpoint} from '~/components/APIEndPoint'

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
            description:'',
            username: "test",
            endpoint: endpoint,
            colorR: 0,
            colorG: 0,
            colorB: 0,
        }
    },
    computed: {
        truncatedDescription() {
            return this.description.length > 40 ? this.description.substring(0, 40) + '...' : this.description;
        },
        iconStyle() {
            return {
                backgroundColor: `rgb(${this.colorR}, ${this.colorG}, ${this.colorB})`,
            };
        }
    },
    async created() {
        const response = await fetch(endpoint+`idea/${this.id}`, {
        })
        const data = await response.json()
        this.title = data.idea.title
        this.description = data.idea.description
        this.username = data.username
        this.imagefilename = data.idea.image

        const userResponse = await fetch(endpoint + `user/`+ this.username);
            const userData = await userResponse.json();
            this.colorR = userData.user.colorR;
            this.colorG = userData.user.colorG;
            this.colorB = userData.user.colorB;
    },
}

</script>