<template>
    <header :class="{ hidden: isHidden }">
        <!-- ヘッダーの内容 -->
        <h1>P<span class="red">!</span>NT</h1>
</header>
</template>

<script>
export default {
    data() {
        return {
            isHidden: false,
            lastScrollY: 0
        };
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll() {
            const currentScrollY = window.scrollY;
            this.isHidden = currentScrollY > this.lastScrollY;
            this.lastScrollY = currentScrollY;
        }
    }
};
</script>

<style scoped>
.hidden {
    transform: translateY(-100%);
    transition: transform 0.3s ease-in-out;
}

header {
    position: fixed;
    top: 0;
    width: 100%;
    background-color: #fff;
    text-align: center;
}
.red {
    color: red;
}
</style>