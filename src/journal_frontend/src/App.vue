<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- <h1>HelloWorld</h1>
  <Items :items="items"/> -->
  <div class="container">
    <JournalItems @flip-completion="flipCompletion" :journal_items="journal_items"/>
  </div>

</template>

<script>
import JournalItems from './components/JournalItems'

export default {
  name: 'App',  
  components: {
    JournalItems
  },
  data() {
    return {
      journal_items: [],
    }
  },
  created() {
    this.journal_items = [
      {
        id: 1,
        title: "Gym",
        note: "push day",
        checkmark: true
      },
      {
        id: 2,
        title: "Reading",
        note: "Cryptonomicon, Neal Stephenson",
        checkmark: false
      },
      {
        id: 3,
        title: "shopping",
        note: "need new shoes",
        checkmark: null
      },
    ]
  },
  methods: {
    flipCompletion(id) {
      console.log(id)
      this.journal_items = this.journal_items.map((journal_item) => journal_item.id === id ? {
        ...journal_item, checkmark: !journal_item.checkmark} : journal_item
      )
      console.log(this.journal_items)
    }
  }
}
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
