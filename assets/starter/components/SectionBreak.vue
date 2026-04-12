<script setup lang="ts">
defineProps<{
  eyebrow?: string
  title: string
  summary?: string
}>()
</script>

<template>
  <section class="section-break">
    <p v-if="eyebrow" class="section-break__eyebrow">{{ eyebrow }}</p>
    <h2 class="section-break__title">{{ title }}</h2>
    <p v-if="summary" class="section-break__summary">{{ summary }}</p>
  </section>
</template>
