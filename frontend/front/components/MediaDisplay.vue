
<template>
  <div class="media-display" v-if="media">
    <img v-if="mediaType === 'image'" :src="media" alt="Media Content" />
    <video v-if="mediaType === 'video'" controls :src="media"></video>
  </div>
</template>

<script>
export default {
  props: {
    media: {
      type: String,
      required: true,
    },
    mediaType: {
      type: String,
      required: true,
    },
  },
};
</script>

<style>
.media-display img,
.media-display video {
  max-width: 100%;
  margin-top: 10px;
}
</style>
