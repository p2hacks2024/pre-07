<template>
  <button
    :class="['btn', variant, { disabled }]"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary', // primary, secondary, danger, etc.
  },
  disabled: {
    type: Boolean,
    default: false,
  },
});
</script>

<style scoped>
.btn {
  padding: 0.5em 1em;
  border-radius: 4px;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}
.btn.primary {
  background-color: #1da1f2;
  color: white;
}
.btn.secondary {
  background-color: #f5f8fa;
  color: #1da1f2;
}
.btn.danger {
  background-color: #e0245e;
  color: white;
}
.btn.disabled {
  background-color: #e0e0e0;
  color: #a0a0a0;
  cursor: not-allowed;
}
</style>
