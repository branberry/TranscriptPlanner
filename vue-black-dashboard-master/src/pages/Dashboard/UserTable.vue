<template>
  <base-table :data="table.data"
              :columns="table.columns"
              thead-classes="text-primary">
  </base-table>
</template>
<script>
  import { BaseTable } from "@/components";


  var blah = {
    title: "Hello",
    columns : [],
    data: []
  };

  export default {
    components: {
      BaseTable
    },
    computed: {
      table(){
        console.log(this.$t('dashboard.usersTable'))
        console.log(blah)
        return this.$t('dashboard.usersTable');
      }
    }   
  }
</script>
<style>
</style>
