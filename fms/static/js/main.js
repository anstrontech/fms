$(document).ready(e => {
    $('#datatable').DataTable()
    $("#faculty_select").on("change", function(e) {
        let formData = new FormData()
        formData.append('faculty', $(this).val())
        formData.append('course', $(this).data('course'))
        formData.append('semester', $(this).data('semester'))
        $.ajax({
            url: "http://127.0.0.1:8000/get_faculty_subject/",
            type: "POST",
            headers: { 'X-CSRFToken': $("#csrf_toek").val() },
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                $("#faculty_subjects").html("")
                $("#faculty_subjects").append(`<option value="">Choose Subjects</option>`)
                $.each(data, function(_, res) {
                    $("#faculty_subjects").append(`<option value="${res.subjectID}">${res.subjectName}</option>`)
                })
            },
        });
    })
})