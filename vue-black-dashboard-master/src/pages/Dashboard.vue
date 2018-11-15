<template>
  <div>
      <base-table :data="tableInformation.tableData"
            :columns="tableInformation.columns">
        <template slot="columns">
          <th class="text-center">#</th>
          <th>Name</th>
          <th>Job Position</th>
          <th>Since</th>
          <th class="text-right">Salary</th>
          <th class="text-right">Actions</th>
        </template>  
        <template slot-scope="{row}">
          <td>{{row.id}}</td>
          <td>{{row.name}}</td>
          <td>{{row.job}}</td>
          <td>{{row.since}}</td>
          <td>{{row.salary}}</td>
          <td class="td-actions text-right">
            <base-button type="info" size="sm" icon>
              <i class="tim-icons icon-single-02"></i>
            </base-button>
            <base-button type="success" size="sm" icon>
              <i class="tim-icons icon-settings"></i>
            </base-button>
            <base-button type="danger" size="sm" icon>
              <i class="tim-icons icon-simple-remove"></i>
            </base-button>
          </td>
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

  let tableInformation;

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
     tableInformation : { columns: ["id", "name", "job", "since", "salary", "actions"],
        tableData: [
          {
            id: 1,
            name: "	Andrew Mike",
            salary: "€ 99,225	",
            job: "Develop",
            since: 2013,
          },
          {
            id: 2,
            name: "	John Doe",
            salary: "€ 89,241",
            job: "Design",
            since: 2012,
          },
          {
            id: 3,
            name: "Alex Mike",
            salary: "€ 92,144	",
            job: "Design",
            since: 2010
          }
        ]
      }
    }
  },
    computed: {

    },
    methods: {

    },
    mounted() {

    },
    beforeDestroy() {

    }
  };
</script>
<style>
</style>
