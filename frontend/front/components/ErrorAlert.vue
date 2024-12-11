<template>
  <div v-if="message" class="error-alert">
    {{ message }}
  </div>
</template>

<script setup>
defineProps({
  message: {
    type: String,
    default: '',
  },
});
</script>

<style scoped>
.error-alert {
  background-color: #e0245e;
  color: white;
  padding: 1em;
  border-radius: 4px;
  font-size: 0.9rem;
  text-align: center;
}
</style>
