

<template>

   <div>
      <div>
         <h1>Transcript Request</h1>
         <form @submit.prevent="handleSubmit">
            <label>
            <textarea rows="10" cols="3" type="text" placeholder="RLN257 NUR850 BIO474 MUP122 SPA331 SPA335 MUP391 HPE499 ENL532 . . ." v-model="user.name"/>
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
           name: '',
         }
       }
     },
   
     methods: {
       handleSubmit() {
         // Send data to the server or update your stores and such.
       }
     }
   }
</script>

<style lang="sass">
</style>

