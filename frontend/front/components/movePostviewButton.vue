<template>
    <div class="circle" @click="movePostview">
        <img src="@/assets/lightbulb.png" alt="lightbulb">
</div>
</template>
<style scoped>
.circle {
    width: 80px;
    height: 80px;
    background-color: #fff7a1;
    border-radius: 50%;
    position: fixed;
    right: 25px;
    bottom: 10%;
}
img {
    width: 60px;
    height: 60px;
    transform: translateX(-6px) translateY(-6px);
    margin: 15px;
}
</style>
<script lang="ts">
export default {
    name: 'movePostviewButton',
    methods: {
        movePostview() {
            this.$router.push('/post');
        },
    },
};
</script>