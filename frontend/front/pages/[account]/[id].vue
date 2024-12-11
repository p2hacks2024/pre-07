<template>
  <div>
    {{post}}
  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    const { data } = await $axios.get(
      `http://10.124.75.43:8000/api/ideas/{params.id}`
    );
    return { post: data };
  },
}
</script>