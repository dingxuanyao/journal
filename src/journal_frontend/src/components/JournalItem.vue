<template>
  <div class="task" >
    <div class="info">
      <h3>{{ journal_item.title }}</h3>
      <p>{{ journal_item.note }}</p>
    </div>
    <div class="checkbox">
      <input type="checkbox" @change="flipCompletion(journal_item.id)" />
    </div>
  </div>
</template>

<script>
export default {
  name: "JournalItem",
  props: {
    journal_item: Object,
  },
  methods: {
    flipCompletion(id) {
      this.$emit("flip-completion", id);
    },
  },
  emits: ["flip-completion"],
};
</script>

<style>
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
  flex: 80%;
}
.checkbox {
  flex: 20%;
}
</style>
