document.addEventListener('DOMContentLoaded', function() {
    const thropicForm = document.getElementById('thropicForm');
    const submitBtn = document.getElementById('submitBtn');
    const sentimentForm = document.getElementById('sentimentForm');
    const sentimentSubmitBtn = document.getElementById('sentimentSubmitBtn');
    const modalBody = document.getElementById('modalBody');
    const submissionModal = new bootstrap.Modal(document.getElementById('submissionModal'));

    submitBtn.addEventListener('click', function() {
        const formData = new FormData(thropicForm);

        fetch('/rag-api', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                modalBody.textContent = JSON.stringify(data.error, null, 2);
            } else {
                modalBody.textContent = JSON.stringify(data.message, null, 2);
            }
            submissionModal.show(); // Show the modal
        })
        .catch(error => {
            modalBody.textContent = 'An error occurred';
            submissionModal.show(); // Show the modal even if there's an error
        });
    });

    sentimentSubmitBtn.addEventListener('click', function() {
        const formData = new FormData(sentimentForm);

        fetch('/rag-api-sentiment', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                modalBody.textContent = JSON.stringify(data.error, null, 2);
            } else {
                modalBody.textContent = JSON.stringify(data.message, null, 2);
            }
            submissionModal.show(); // Show the modal
        })
        .catch(error => {
            modalBody.textContent = 'An error occurred';
            submissionModal.show(); // Show the modal even if there's an error
        });
    });
});

document.getElementById('confirmSubmit').addEventListener('click', function() {
    var form = document.querySelector('form');
    form.submit(); // Submit the form
});

document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function() {
        var filename = this.getAttribute('data-filename');
        var downloadLink = document.getElementById('downloadLink');
        downloadLink.href = `/download_plate/${filename}`;
        var dropdownButton = document.getElementById('dropdownMenuButton');
        dropdownButton.textContent = this.textContent;
    });
});

$(document).ready(function() {
    // Function to check if the element is in viewport
    function isElementInView(element) {
        var elementTop = $(element).offset().top;
        var elementBottom = elementTop + $(element).outerHeight();

        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();

        return elementBottom > viewportTop && elementTop < viewportBottom;
    }

    // Listen for scroll events
    $(window).on('scroll', function() {
        // Check if the carousel is in view
        if (isElementInView($('#carouselExample'))) {
            // Add class to fade in
            $('#carouselExample').addClass('fade-in');
        }
        // Check each invisible section and fade in if in view
        $('.invisible-section').each(function() {
            if (isElementInView($(this))) {
                $(this).addClass('fade-in');
            }
        });
    });

    // Trigger the scroll event on page load in case the carousel is already in view
    $(window).scroll();

    // Border appearance on hover for text columns
    $('.col.fs-4 p').hover(
        function() {
            // Mouse enters column area
            $(this).addClass('box-color3 fs-3').removeClass('fs-4');
        }, 
        function() {
            // Mouse leaves column area
            $(this).removeClass('box-color3 fs-3').addClass('fs-4');
        }
    );

    $('.card').hover(
        function() {
            // Mouse enters the card area
            $(this).addClass('highlighted');
        },
        function() {
            // Mouse leaves the card area
            $(this).removeClass('highlighted');
        }
    );

    // Content highlight
    $('.card.box-color3.rounded-5.border-dark').hover(
        function() {
            // Mouse enters the card area
            $(this).addClass('highlighted');
        },
        function() {
            // Mouse leaves the card area
            $(this).removeClass('highlighted');
        }
    );

    $('#confirmSubmit').click(function() {
        $('form').submit(); // Submit the form
    });

    $('.dropdown-item').click(function() {
        var filename = $(this).attr('data-filename');
        var downloadLink = $('#downloadLink');
        downloadLink.attr('href', `/download_plate/${filename}`);
        $('#dropdownMenuButton').text($(this).text());
    });
});
