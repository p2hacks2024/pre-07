<template>
    <div class="search">
        <input
        type="text"
        id="serchText"
        :placeholder="textMessage"
        v-model="searchText"
        >
    </div>
</template>

<script>
export default {
    props:{
        textMessage: {
            type: String,
            default: ''
        },
    },
    data () {
        return {
            searchText: {
                type: String,
                default: ''
            },
        }
    },
}
</script>

<style scoped>
.search {
    text-align: center;

}
.search input {
    font-size: 16px;
    border: 1px solid #fff;
    background-color: rgb(224, 224, 224);
    padding: 15px 30px;
    border-radius: 15px;
    width: 60%;
}
</style>