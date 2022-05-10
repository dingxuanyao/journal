<template>
  <div>
    <div :key="journal_item.id" v-for="journal_item in journal_items">
      <JournalItem
        @flip-completion="flipCompletion"
        :journal_item="journal_item"
      />
    </div>
  </div>
</template>

<script>
import JournalItem from "./JournalItem";
export default {
  name: "JournalItems",
  props: {
    journal_items: Array,
  },
  components: {
    JournalItem,
  },
  methods: {
    flipCompletion(id) {
      this.$emit("flip-completion", id);
    },
  },
  emits: ["flip-completion"],
};
</script>
