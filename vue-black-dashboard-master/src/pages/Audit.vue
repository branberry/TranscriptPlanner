<template>
<div>

    <div>
        <h1>Audit Your Transcript</h1>

        <div>
            <h4>Upload your transcipt here</h4>
            <form enctype="multipart/form-data">
                <input type="file" multiple :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name,$event.target.files); fileCount = $event.target.files.length">
            </form>
        </div>

    </div>

</div>
</template>
<script>
    import axios from 'axios';



    const BASE_URL = "http://localhost:5000"
    const STATUS = {
        INITIAL: 0,
        SAVING: 1,
        SUCCESS: 2,
        FAILED: 3
    }

    /**
     * This function handles the uploading of form data to the backend
     */
    const upload = formData => {
        const url = `${BASE_URL}/transcript/upload`;
    }

    export default {
        data() {
            return {
                uploadedFiles: [],
                uploadError: null,
                currentStatus: null,
                uploadFieldName: 'transcript'
            }
        },

        computed: {

            isInitial() {
                return this.currentStatus = STATUS.INITIAL;
            },

            isSaving() {
                return this.currentStatus = STATUS.SAVING;
            },

            isSuccess() {
                return this.currentStatus = STATUS.SUCCESS;
            },

            isFailed() {
                return this.currentStatus = STATUS.FAILED;
            }
        },
        methods: {
            /**
             * Reset the form to its initial state!
             */
            reset() {
                this.currentStatus = STATUS.INITIAL;
                this.uploadedFiles = [];
                this.uploadError = null;
            },

            save(formData) {
                this.currentStatus = STATUS.SAVING;

                upload(formD)
            }
        }
    }
</script>
<style lang="sass">
</style>