<template>
	<div>
		<div>
			<h1>Transcript Request</h1>

			<h3>Course Catalog List</h3>
			<base-dropdown title-classes="btn btn-secondary"
               title="Add a Course" >

					<option v-for="course in courses" v-bind:key="course.id" class="dropdown-item" v-bind:value="course" @click="addCourse(course)">{{course.courseNum}}</option>

			</base-dropdown>
			<div>
				<br>
				<h3>Selected Courses</h3>

						<base-table :data="user.courses"
										>
								<template slot="columns">
									<th class="text-center">#</th>
									<th>Name</th>
									<th>Credits</th>
									<th>Prerequisites</th>
									<th>Course Number</th>
									<th>Offered In</th>      
									<th>Department</th>
									<th>Description</th>
									<th></th> 
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
									<td> <button v-on:click="removeCourse(row)">Remove</button> </td>
								</template>    
						</base-table>
			</div>
			<br>
			<a id="dummy"></a>
			<button id="dwn" v-on:click="downloadCSV()">Download as CSV</button>
			<button id="dwn" v-on:click="downloadJSON()">Download as JSON</button>
		</div>
	</div>
</template>
<script>
	import axios from 'axios';
	import { BaseTable } from "@/components";


	export default {
		components: {
				BaseTable
		},
		
	  data() {
	    return {
	      user: {
	        courses: []

	      },

				courses: [],

				columns: ["id", "name", "credits", "offeredIn", "description", "department"]
      
	    }
	  },
	   
		methods: {
			
			addCourse(course) {
				console.log(course);
				this.user.courses.push(course);
				console.log(this.user);
			},
			removeCourse(inf) {

				var index = this.user.courses.indexOf(inf);
				if (index > -1) {
       				this.user.courses.splice(index, 1);
    			}

			},
			downloadCSV() {
					var csv = 'ID,name,credits,prereqs,courseNum,offeredIn,description,department\r\n';
					this.user.courses.forEach(function(row) {
									csv += row.id + ',"' + row.name + '",' + row.credits + ',"'  + row.prereqs + '",' + row.courseNum + ',' + row.offeredIn + ',"' + row.description + '",' + row.department ;
									csv += "\r\n";
					});

					var hiddenElement = document.getElementById('dummy');
					hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
					hiddenElement.target = '_blank';
					hiddenElement.download = 'courses.csv';
					hiddenElement.click();


			},
			downloadJSON() {

					var major /* set major here */;
					var json = ' {\r\n\t"transcript": {\r\n\t\t"major": "' + major + '",\r\n\t\t"courses": [';
				
					this.user.courses.forEach(function(row) {
						json += '\r\n\t\t"' + row.courseNum + '",'
					});
					json = json.substring(0, json.length-1);
					json += '\r\n\t\t]\r\n\t}\r\n}'
			
					var hiddenElement = document.getElementById('dummy');
					hiddenElement.href = 'data:text/json;charset=utf-8,' + encodeURI(json);
					hiddenElement.target = '_blank';
					hiddenElement.download = 'courses.json';
					hiddenElement.click();
			}
		},

    mounted() {
      axios
        .get("http://127.0.0.1:5000/catalog")
        .then( res => {

          return JSON.parse(res.data);

        })
        .then(res => {
          this.courses = res.courses;
        });

		 }
	}
</script>
<style lang="scss">

button { 
    background-color: rgb(56, 239, 125);
    border: none;
    color: black;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

#dwn{
	padding: 2em;
	margin-right: 1em;
	margin-top: 1em;
}

</style>

