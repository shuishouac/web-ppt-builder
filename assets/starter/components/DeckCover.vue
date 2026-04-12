<script setup lang="ts">
defineProps<{
  title: string
  subtitle?: string
  presenter?: string
  role?: string
  organization?: string
  logo?: string
  headshot?: string
  showLogo?: boolean
  showHeadshot?: boolean
}>()
</script>

<template>
  <section class="deck-cover">
    <div class="deck-cover__top">
      <img
        v-if="showLogo && logo"
        :src="logo"
        alt="logo"
        class="deck-cover__logo"
      >
      <div v-else class="deck-cover__eyebrow">
        Web-first presentation
      </div>
    </div>

    <div class="deck-cover__body">
      <div class="deck-cover__copy">
        <p class="deck-cover__kicker">Presentation Website</p>
        <h1 class="deck-cover__title">{{ title }}</h1>
        <p v-if="subtitle" class="deck-cover__subtitle">{{ subtitle }}</p>

        <div class="deck-cover__meta">
          <div v-if="presenter" class="deck-cover__person">{{ presenter }}</div>
          <div v-if="role || organization" class="deck-cover__role">
            {{ [role, organization].filter(Boolean).join(" · ") }}
          </div>
        </div>
      </div>

      <div v-if="showHeadshot && headshot" class="deck-cover__portrait-wrap">
        <img :src="headshot" alt="presenter headshot" class="deck-cover__portrait">
      </div>
    </div>
  </section>
</template>
