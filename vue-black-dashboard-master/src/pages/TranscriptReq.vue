<template>
	<div>
		<div>
			<h1>Transcript Request</h1>

			<h3>Course Catalog List</h3>
			<base-dropdown title-classes="btn btn-secondary"
               title="Add a Course">

					<a v-for="course in courses" v-bind:key="course.id" class="dropdown-item" href="#">{{course.courseNum}}</a>

			</base-dropdown>
			<form @submit.prevent="handleSubmit">

				<br>
				<button type="submit">Submit</button>
			</form>
		</div>
	</div>
</template>
<script>
  import axios from 'axios';

	export default {
	  data() {
	    return {
	      user: {
	
	        classes: ''
	       
	        
	      },

				courses: []
	    }
	  },
	   
		methods: {
			handleSubmit() {
				var classIn = this.user.classes;
				var classArr = classIn.split("\n");

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

