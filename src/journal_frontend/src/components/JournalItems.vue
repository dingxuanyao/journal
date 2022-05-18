<template>
  <div>
    <div :key="journal_item.id" v-for="journal_item in journal_items">
      <JournalItem
        @flip-completion="flipCompletion"
        @delete-journal-item="deleteJournalItem"
        @update-journal-item="updateJournalItem"
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
    updateJournalItem(id, journal_item_updated) {
      this.$emit("update-journal-item", id, journal_item_updated);
    },
    flipCompletion(id) {
      this.$emit("flip-completion", id);
    },
    deleteJournalItem(id) {
      this.$emit("delete-journal-item", id);
    },
  },
  emits: ["flip-completion", "delete-journal-item", "update-journal-item"],
};
</script>
