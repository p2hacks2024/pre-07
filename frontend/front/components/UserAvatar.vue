<template>
  <div class="user-avatar">
    <img :src="user.avatar" alt="User Avatar" />
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>
.user-avatar img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 2px solid #ccc;
}
</style>
