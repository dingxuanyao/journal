<template>
  <div class="task">
    <div class="info">
      <input
        class="modern title"
        v-model="journal_item_local.title"
        @input="onInput(journal_item.id)"
      />
      <input
        class="modern note"
        v-model="journal_item_local.note"
        @input="onInput(journal_item.id)"
      />
    </div>
    <div class="checkbox">
      <input
        type="checkbox"
        v-show="journal_item.checkmark !== null"
        :checked="journal_item_local.checkmark"
        v-model="journal_item_local.checkmark"
        @change="onInput(journal_item.id)"
      />
    </div>
    <div class="delete">
      <button class="delete-button" @click="deleteJournalItem(journal_item.id)">
        X
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "JournalItem",
  data() {
    return {
      journal_item_local: {
        title: this.journal_item.title,
        id: this.journal_item.id,
        note: this.journal_item.note,
        checkmark: this.journal_item.checkmark,
      },
    };
  },
  props: {
    journal_item: Object,
  },
  methods: {
    updateJournalItem(id) {
      this.$emit("update-journal-item", id, this.journal_item_local);
    },
    onInput(id) {
      this.updateJournalItem(id);
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

<style>
@import url("https://fonts.googleapis.com/css?family=Roboto");
@import url("https://fonts.googleapis.com/css?family=Andada|Permanent+Marker|Raleway:300");
.task {
  display: flex;
  flex-wrap: wrap;
  background: gainsboro;
  margin: 5px;
  padding: 10px 20px;
}
.task:after {
  content: "";
  display: table;
  clear: both;
}
.task h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.info {
  flex: 60%;
}
.checkbox {
  flex: 20%;
}
.delete {
  flex: 20%;
}
.delete-button {
  border: 1px solid darkred;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
.delete-button:hover {
  cursor: pointer;
  background-color: red;
}
input {
  border: 0;
  padding: 10px;
  width: 100%;
  background: transparent;
}
.title {
  font-size: 20px;
}
</style>
