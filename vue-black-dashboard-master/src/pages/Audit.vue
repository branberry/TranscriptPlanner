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
        const url = `${BASE_URL}/transcript`;

        return axios.post(url, formData)
            // retrieve data
            .then(res => res.data)
            .then(res => {
                console.log(res);
            })
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

            /**
             * Takes the form data, and sends it to the backend
             * the status is updated accordingly
             */
            save(formData) {
                this.currentStatus = STATUS.SAVING;

                upload(formData)
                    .then(res => {
                        this.uploadedFiles = [].concat(res);
                        this.currentStatus = STATUS.SUCCESS;
                    })
                    .catch(err => {
                        this.uploadError = err.response;
                        this.currentStatus = STATUS.FAILED;
                    });
            },

            filesChange(fieldName, fileList) {

                // handle file changes
                const formData = new FormData();

                if (!fileList.length) return;

                // append the files to the FormData object

                Array.from(Array(fileList.length).keys())
                    .map(x => {
                        formData.append(fieldName, fileList[x], fileList[x].name);
                    });
                
                // save the form data!
                this.save(formData);
            },

            mounted() {
                this.reset();
            }
        }
    }
</script>
<style lang="sass">
</style>