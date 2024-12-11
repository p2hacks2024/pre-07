<template>
  <div class="spinner" :style="{ width: size, height: size }"></div>
</template>

<script setup>
defineProps({
  size: {
    type: String,
    default: '40px',
  },
});
</script>

<style scoped>
.spinner {
  border: 4px solid rgba(0, 0, 0, 0.2);
  border-top-color: #1da1f2;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
