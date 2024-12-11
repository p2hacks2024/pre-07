<template>
  <div class="page">
      {{ message }}
  </div>
</template>

<script>
export default {
  data() {
      return {
          message: ''
      }
  },
  async created() {
      const response = await fetch('http://10.124.75.43:8000')
      const data = await response.json()
      this.message = data.Hello
  },
}
</script>