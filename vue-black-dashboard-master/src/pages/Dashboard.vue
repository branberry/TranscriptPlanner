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
     tableInformation : { columns: ["id", "name", "credits", "offeredIn", "description", "department"],
        tableData: [
          {
            id: 1,
            name: "	Themes in American Indian Literature",
            credits: 4,
            prereqs: "Prerequisite(s): None",
            courseNum: "AIS355",
            offeredIn: null,
            description: "The course is structured around a number of writers working within a particular theme such as Native Voices ofMinnesota, Voices from the Southwest, Poetics and Politics of Native Writing, Women and Power in Native Literature,Urban-Reservation: Homing, and American Indian film-literature adaptation. Students focus on primary texts, comparingand contrasting theme, voice, aesthetic, or cultural emphasis as it shifts or arises across the group of texts. Course crosslists with English.",
            department: "AIS"
          },
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
