<template>
  <div class="container">
    <JournalItems
      @flip-completion="flipCompletion"
      @delete-journal-item="deleteJournalItem"
      @update-journal-item="updateJournalItem"
      :journal_items="journal_items"
    />
  </div>
</template>

<script>
import JournalItems from "./components/JournalItems";

export default {
  name: "App",
  components: {
    JournalItems,
  },
  data() {
    return {
      journal_items: [],
    };
  },
  created() {
    this.journal_items = [
      {
        id: 1,
        title: "Gym",
        note: "push day",
        checkmark: true,
      },
      {
        id: 2,
        title: "Reading",
        note: "Cryptonomicon, Neal Stephenson",
        checkmark: false,
      },
      {
        id: 3,
        title: "shopping",
        note: "need new shoes",
        checkmark: null,
      },
    ];
  },
  methods: {
    updateJournalItem(id, journal_item_updated) {
      this.journal_items = this.journal_items.map((journal_item) =>
        journal_item.id === id
          ? journal_item_updated
          : journal_item
      );
      const log_item = this.journal_items.filter((journal_item) => journal_item.id == id)      
      console.log(log_item[0])
    },
    deleteJournalItem(id) {
      this.journal_items = this.journal_items.filter((journal_item) => journal_item.id !== id)
    },
    flipCompletion(id) {
      this.journal_items = this.journal_items.map((journal_item) =>
        journal_item.id === id
          ? {
              ...journal_item,
              checkmark: !journal_item.checkmark,
            }
          : journal_item
      );
      console.log(this.journal_items);
    },
  },
};
</script>

<style>
.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
</style>
