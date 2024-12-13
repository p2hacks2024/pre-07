<script>
import textBox from '~/components/textBox.vue'
</script>

<template>
    <div class="topText">
            <p>他の人のアイディアを<br>
            見てみましょう</p><br>
        </div>
        <textBox textMessage="アイデアを検索"></textBox>
</template>


<style scoped>

p{
    text-align: center;
}
.topText{
    padding: 50px;
    margin-top: 50px;
}

</style>
