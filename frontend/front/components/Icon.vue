<script>
import { endpoint } from '~/components/APIEndPoint';

export default {
    props: {
        username: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            colorR: 0,
            colorG: 0,
            colorB: 0,
        }
    },
    async created() {
        console.log(this.username);
        try {
            const userResponse = await fetch(endpoint + `user/`+ this.username);
            const userData = await userResponse.json();
            this.colorR = userData.user.colorR;
            this.colorG = userData.user.colorG;
            this.colorB = userData.user.colorB;
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    },
    computed: {
        iconStyle() {
            return {
                backgroundColor: `rgb(${this.colorR}, ${this.colorG}, ${this.colorB})`,
            };
        }
    }
}
</script>

<template>
    <div class="icon" :style="iconStyle">
        <span class="icon-text">{{ username ? username.charAt(0) : '' }}</span>
    </div>
</template>


<style scoped>
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