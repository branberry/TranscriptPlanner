<template>
  <div>
    <base-table :data="tableInformation.tableData"
            :columns="tableInformation.columns">
        <template slot="columns">
          <th class="text-center">#</th>
          <th>Name</th>
          <th>Credits</th>
          <th>Prerequisites</th>
          <th>Course Number</th>
          <th>Offered In</th>      
          <th>Department</th>
          <th>Description</th> 
        </template>  
        <template slot-scope="{row}">
          <td>{{row.id}}</td>
          <td>{{row.name}}</td>
          <td>{{row.credits}}</td>
          <td>{{row.prereqs}}</td>
          <td>{{row.courseNum}}</td>
          <td>{{row.offeredIn}}</td>
          <td>{{row.department}}</td>
          <td>{{row.description}}</td>
        </template>    
    </base-table>
  </div>
</template>
<script>
  import LineChart from '@/components/Charts/LineChart';
  import BarChart from '@/components/Charts/BarChart';
  import * as chartConfigs from '@/components/Charts/config';
  import TaskList from './Dashboard/TaskList';
  import UserTable from './Dashboard/UserTable';
  import CourseTable from './Dashboard/CourseTable';
  import config from '@/config';
  import axios from 'axios';
  import { BaseTable } from "@/components";

  var tableInformation;

  export default {
    components: {
      LineChart,
      BarChart,
      TaskList,
      UserTable,
      CourseTable,
      BaseTable
      
    },
      
    data() {
      return {
      tableInformation : { columns: ["id", "name", "credits", "offeredIn", "description", "department"],
          tableData: []
        }
      }
    },
    
    computed: {

    },
    methods: {

    },
    mounted() {
      axios
        .get("http://127.0.0.1:5000/catalog")
        .then( res => {

          return JSON.parse(res.data);

        })
        .then(res => {
          this.tableInformation['tableData'] = res.courses;
        });

    },
    beforeDestroy() {

    }
  };
</script>
<style>
</style>
