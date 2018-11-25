<template>
	<div>
		<div>
			<h1>Transcript Request</h1>
			<form @submit.prevent="handleSubmit">
				<label>
				<textarea rows="10" cols="3" type="text" placeholder="RLN257 NUR850 BIO474 MUP122 SPA331 SPA335 MUP391 HPE499 ENL532 . . ." v-model="user.classes"/>
				</label>
				<br>
				<button type="submit">Submit</button>
			</form>
		</div>
	</div>
</template>
<script>
	export default {
	  data() {
	    return {
	      user: {
	
	        classes: ''
	       
	        
	      }
	    }
	  },
	   
	     methods: {
	       handleSubmit() {
	           var classIn = this.user.classes;
	            var classArr = classIn.split("\n");
	
	
	
	
	
	       }
	     }
	   }
</script>
<style lang="sass">

.button { 
    background-color: rgb(56, 239, 125)
    border: none
    color: white
    padding: 15px 20px
    text-align: center
    text-decoration: none
    display: inline-block
    font-size: 16px
    margin: 4px 2px
    cursor: pointer
}

</style>

