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
									<td class="td-actions text-right">
										<base-button type="danger" size="sm" icon @click="removeCourse(row.id)">
											<i class="tim-icons icon-simple-remove"></i>
										</base-button>
         					 </td>
								</template>    
						</base-table>
			</div>
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

			removeCourse(id) {
				for (let i = 0; i < this.user.courses.length; i++) {
					if (this.user.courses[i].id === id) {
						this.user.courses.splice(i,1);
					}
				}
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

.button { 
    background-color: rgb(56, 239, 125);
    border: none;
    color: white;
    padding: 15px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

</style>

