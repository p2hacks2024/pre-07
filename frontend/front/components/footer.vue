<template>
    <div>
        <a href="/home">
            <img src="@/assets/home.png" alt="home" />
        </a>
        <a href="#">
            <img src="@/assets/folder.png" alt="folder" />
        </a>
        <a href="/search">
            <img src="@/assets/search.png" alt="search" />
        </a>
        <a href="#">
            <img src="@/assets/brain.png" alt="brain" />
        </a>
        <a href="#">
            <img src="@/assets/human.png" alt="human" />
        </a>
    </div>
</template>
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
    z-index: 1000;
}

img {
    width: 30px;
}
</style>