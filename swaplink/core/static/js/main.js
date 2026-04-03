// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Sticky Header with Scroll Effect
    const header = document.getElementById('mainHeader');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }
    
    // 2. Mobile Menu Toggle
    const menuBtn = document.getElementById('menuBtn');
    const mobileNav = document.getElementById('mobileNav');
    
    if (menuBtn && mobileNav) {
        menuBtn.addEventListener('click', function() {
            mobileNav.classList.toggle('open');
            const icon = menuBtn.querySelector('i');
            if (mobileNav.classList.contains('open')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // 3. Close mobile menu when clicking a link
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');
    mobileLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileNav.classList.remove('open');
            const icon = menuBtn.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        });
    });
    
    // 4. Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // 5. Add fade-in animation on scroll (Intersection Observer)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Apply fade-in to sections
    const sections = document.querySelectorAll('.products-preview, .audience, .philosophy, .cta-section');
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
    
    // 6. Animate product cards on hover with cursor effect
    const cards = document.querySelectorAll('.product-card, .audience-block');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function(e) {
            this.style.transition = 'all 0.3s cubic-bezier(0.2, 0.9, 0.4, 1.1)';
        });
    });
    
    // Product logo click navigation - redirect to product pages
const logoItems = document.querySelectorAll('.logo-item');
if (logoItems.length > 0) {
    logoItems.forEach(item => {
        item.addEventListener('click', function() {
            const product = this.getAttribute('data-product');
            if (product === 'marketplace') {
                window.location.href = '/products/marketplace/';
            } else if (product === 'events') {
                window.location.href = '/products/events/';
            } else if (product === 'egift') {
                window.location.href = '/products/egift/';
            } else if (product === 'payroll') {
                window.location.href = '/products/payroll/';
            }
        });
    });
}



    // Simple and reliable active link detection
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');

navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');
    
    // Remove any existing active class
    link.classList.remove('active');
    
    // Exact match for root path
    if (linkPath === '/' && currentPath === '/') {
        link.classList.add('active');
    }
    // Exact match for other paths
    else if (linkPath !== '/' && currentPath === linkPath) {
        link.classList.add('active');
    }
    // Handle trailing slash differences
    else if (linkPath !== '/' && currentPath === linkPath + '/') {
        link.classList.add('active');
    }
});
    
    // 8. Dynamic cursor glow effect (optional techy feel)
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        document.addEventListener('mousemove', function(e) {
            const mouseX = e.clientX;
            const mouseY = e.clientY;
            const heroRect = heroSection.getBoundingClientRect();
            
            if (mouseY >= heroRect.top && mouseY <= heroRect.bottom) {
                const xPercent = (mouseX / window.innerWidth) * 100;
                const yPercent = (mouseY / window.innerHeight) * 100;
                heroSection.style.background = `radial-gradient(circle at ${xPercent}% ${yPercent}%, #ffffff 0%, #f8f9fa 100%)`;
            }
        });
    }
    
    // 9. Console log to confirm JS is loaded (remove in production)
    console.log('SwapLink Integrated - Modern UI Loaded');
});

// Products page filter functionality
const filterTabs = document.querySelectorAll('.filter-tab');
if (filterTabs.length > 0) {
    filterTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs
            filterTabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            this.classList.add('active');
            
            // Get filter value
            const filterValue = this.getAttribute('data-filter');
            
            // Remove existing body classes
            document.body.classList.remove('filter-active', 'filter-coming-soon');
            
            // Add new body class based on filter
            if (filterValue === 'active') {
                document.body.classList.add('filter-active');
            } else if (filterValue === 'coming-soon') {
                document.body.classList.add('filter-coming-soon');
            }
            // 'all' does nothing - shows everything
        });
    });
}
// Get Started Page Form Submission
const signupForm = document.getElementById('signupForm');
const successMessage = document.getElementById('successMessage');
const successEmail = document.getElementById('successEmail');

if (signupForm) {
    signupForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get submit button
        const submitBtn = this.querySelector('.submit-btn');
        submitBtn.classList.add('loading');
        
        // Collect form data
        const formData = {
            account_type: this.querySelector('input[name="account_type"]:checked').value,
            fullname: this.querySelector('#fullname').value,
            email: this.querySelector('#email').value,
            phone: this.querySelector('#phone').value,
            product: this.querySelector('#product').value,
            referral: this.querySelector('#referral').value,
            terms: this.querySelector('input[name="terms"]').checked
        };
        
        try {
            const response = await fetch('/api/submit-interest/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(formData)
            });
            
            const result = await response.json();
            
            if (result.status === 'success') {
                // Hide form, show success message
                signupForm.style.display = 'none';
                if (successMessage) {
                    if (successEmail) {
                        successEmail.textContent = formData.email;
                    }
                    successMessage.style.display = 'block';
                }
            } else {
                alert('Something went wrong. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Network error. Please try again.');
        } finally {
            submitBtn.classList.remove('loading');
        }
    });
}