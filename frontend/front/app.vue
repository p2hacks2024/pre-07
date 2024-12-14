<script setup lang="ts">

</script>
<template>
    <div>
        <Header />
        <div class="space"></div>
        <NuxtPwaManifest />
        <NuxtPage />
        <div class="space"></div>
        <Footer class="footer" />
    </div>
</template>
<style>
body {
    margin: 0;
    padding: 0;
}
.space {
    margin-top: 80px;
}
</style>