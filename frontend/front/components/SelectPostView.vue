<template>
    <div class="postView" @click="emitItemClick">
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
    width: 100%;
    max-height: 100px;
    object-fit: cover;
    border-radius: 20px 20px 0px 0px;
}
h1 {
    font-family: "Zen Kaku Gothic New", sans-serif;
    margin: 0;
    padding: 0;
    font-size: 20px;
}
p {
    align-items: center;
    font-family: "Zen Kaku Gothic New", sans-serif;
    margin: 0;
    padding: 0;
}
.contents {
    padding: 5px;
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
.icon p {

    display: table-cell;
    text-align: center;
    vertical-align: middle;
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
import Icon from '~/components/Icon.vue'
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
            username: '',
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
    methods: {
        emitItemClick() {
            this.$emit('item-click', this.id, this.title, this.description);
        }
    }
}

</script>