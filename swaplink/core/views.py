from django.shortcuts import render
from django.http import JsonResponse
import json

def home(request):
    context = {
        'company_name': 'SwapLink',
        'tagline': 'Integrated',
        'vision': 'A modern tech company building platforms that make life easier — connecting people to trusted services, opportunities, and digital solutions all in one place.',
        'services': [
            'Online Services Platform and Marketplace',
            'Service Aggregation and Booking Systems',
            'Digital Payments Integration',
            'Business Automation Tools',
            'Tech-Enabled Service Delivery',
        ],
        'products': [
            'Services Marketplace',
            'Events and Ticketing',
            'eGift Platform',
            'Smart Payroll and HR',
        ],
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def products(request):
    context = {
        'products_list': [
            {
                'id': 1,
                'name': 'Services Marketplace',
                'tagline': 'Connect with trusted local professionals',
                'description': 'Find and book verified service providers in your area. From plumbers to tutors, photographers to cleaners - all verified and reviewed.',
                'icon': 'fa-store',
                'features': [
                    'Verified professional profiles',
                    'Real customer reviews and ratings',
                    'Instant booking and scheduling',
                    'Secure in-app payments',
                    'Service history and receipts'
                ],
                'for_users': True,
                'for_business': True,
                'status': 'active',
                'learn_more_url': '/products/marketplace/',
                'get_started_url': '/get-started/?product=marketplace'
            },
            {
                'id': 2,
                'name': 'Events and Ticketing',
                'tagline': 'Sell tickets. Manage events. Grow attendance.',
                'description': 'Complete event management platform for organizers and a seamless ticket buying experience for attendees.',
                'icon': 'fa-calendar-alt',
                'features': [
                    'Custom ticket types (VIP, Early Bird, Group)',
                    'QR code check-in system',
                    'Real-time sales analytics',
                    'Email notifications to attendees',
                    'Event pages with maps and schedules'
                ],
                'for_users': True,
                'for_business': True,
                'status': 'active',
                'learn_more_url': '/products/events/',
                'get_started_url': '/get-started/?product=events'
            },
            {
                'id': 3,
                'name': 'eGift Platform',
                'tagline': 'Send instant digital gifts for any occasion',
                'description': 'Create and send beautiful digital gift cards for shopping, dining, services, and more. Perfect for birthdays, holidays, or just because.',
                'icon': 'fa-gift',
                'features': [
                    'Instant email delivery',
                    'Scheduled delivery dates',
                    'Personalized messages and designs',
                    'Wide range of partner merchants',
                    'Bulk sending for businesses'
                ],
                'for_users': True,
                'for_business': True,
                'status': 'active',
                'learn_more_url': '/products/egift/',
                'get_started_url': '/get-started/?product=egift'
            },
            {
                'id': 4,
                'name': 'Smart Payroll and HR',
                'tagline': 'Payroll and HR simplified for small businesses',
                'description': 'Stop using spreadsheets. Automate payroll, manage leave, and keep employee records in one secure dashboard.',
                'icon': 'fa-users',
                'features': [
                    'Automated monthly payslips',
                    'Leave and absence management',
                    'Employee database and documents',
                    'Tax and compliance reporting',
                    'Direct bank transfer integration'
                ],
                'for_users': False,
                'for_business': True,
                'status': 'active',
                'learn_more_url': '/products/payroll/',
                'get_started_url': '/get-started/?product=payroll'
            },
            {
                'id': 5,
                'name': 'Business Automation Tools',
                'tagline': 'Work smarter, not harder',
                'description': 'Automate repetitive tasks, streamline workflows, and integrate your favorite business tools into one seamless experience.',
                'icon': 'fa-robot',
                'features': [
                    'Workflow automation builder',
                    'Third-party app integrations',
                    'Custom reporting dashboards',
                    'Task and project management',
                    'Invoice and payment automation'
                ],
                'for_users': False,
                'for_business': True,
                'status': 'coming-soon',
                'learn_more_url': '/products/automation/',
                'get_started_url': None
            },
            {
                'id': 6,
                'name': 'Digital Payments Hub',
                'tagline': 'One integration for all payment methods',
                'description': 'Accept payments from cards, mobile money, bank transfers, and digital wallets. Single API, unified dashboard.',
                'icon': 'fa-credit-card',
                'features': [
                    'Multiple payment methods',
                    'Recurring billing and subscriptions',
                    'Fraud detection and prevention',
                    'Real-time transaction tracking',
                    'Developer-friendly API'
                ],
                'for_users': False,
                'for_business': True,
                'status': 'coming-soon',
                'learn_more_url': '/products/payments/',
                'get_started_url': None
            },
        ]
    }
    return render(request, 'core/products.html', context)

def get_started(request):
    selected_product = request.GET.get('product', '')
    
    context = {
        'selected_product': selected_product,
        'products_for_select': [
            {'value': 'marketplace', 'label': 'Services Marketplace', 'icon': 'fa-store'},
            {'value': 'events', 'label': 'Events and Ticketing', 'icon': 'fa-calendar-alt'},
            {'value': 'egift', 'label': 'eGift Platform', 'icon': 'fa-gift'},
            {'value': 'payroll', 'label': 'Smart Payroll and HR', 'icon': 'fa-users'},
        ]
    }
    return render(request, 'core/get_started.html', context)

def for_business(request):
    context = {
        'business_products': [
            {
                'name': 'Services Marketplace',
                'description': 'List your services, get verified, and connect with customers looking for what you offer.',
                'icon': 'fa-store',
                'features': ['Verified business profile', 'Customer reviews', 'Booking management', 'Payment processing'],
                'cta_url': '/get-started/?product=marketplace&type=business'
            },
            {
                'name': 'Events and Ticketing',
                'description': 'Sell tickets online, manage check-ins, and grow your event attendance with powerful marketing tools.',
                'icon': 'fa-calendar-alt',
                'features': ['Custom ticket types', 'QR code check-in', 'Sales analytics', 'Email marketing'],
                'cta_url': '/get-started/?product=events&type=business'
            },
            {
                'name': 'eGift Platform',
                'description': 'Offer digital gift cards to your customers. Increase sales and attract new business.',
                'icon': 'fa-gift',
                'features': ['Custom gift card designs', 'Bulk purchasing', 'Customer insights', 'Promotion tools'],
                'cta_url': '/get-started/?product=egift&type=business'
            },
            {
                'name': 'Smart Payroll and HR',
                'description': 'Run payroll, manage employee leave, and keep all HR records in one secure place.',
                'icon': 'fa-users',
                'features': ['Automated payslips', 'Leave management', 'Employee database', 'Tax reporting'],
                'cta_url': '/get-started/?product=payroll&type=business'
            },
        ],
        'business_benefits': [
            {
                'title': 'Save time and money',
                'description': 'Automate repetitive tasks and reduce operational costs by up to 40 percent.',
                'icon': 'fa-chart-line'
            },
            {
                'title': 'Reach more customers',
                'description': 'Get discovered by thousands of potential customers using our platform.',
                'icon': 'fa-chart-simple'
            },
            {
                'title': 'One dashboard, all tools',
                'description': 'Manage all your business operations from a single, intuitive dashboard.',
                'icon': 'fa-tachometer-alt'
            },
            {
                'title': 'Secure and compliant',
                'description': 'Enterprise-grade security with full data protection and compliance.',
                'icon': 'fa-shield-alt'
            },
            {
                'title': '24/7 business support',
                'description': 'Dedicated support team available around the clock for business accounts.',
                'icon': 'fa-headset'
            },
            {
                'title': 'Scale as you grow',
                'description': 'Flexible pricing that grows with your business. No long-term contracts.',
                'icon': 'fa-rocket'
            },
        ],
        'pricing_plans': [
            {
                'name': 'Starter',
                'price': 'Free',
                'period': 'forever',
                'features': [
                    'Up to 10 employees',
                    'Basic payroll features',
                    'Email support',
                    'Limited product listings'
                ],
                'cta_url': '/get-started/?plan=starter',
                'recommended': False
            },
            {
                'name': 'Professional',
                'price': '$29',
                'period': 'per month',
                'features': [
                    'Up to 50 employees',
                    'Full payroll and HR suite',
                    'Priority support',
                    'Unlimited product listings',
                    'Advanced analytics'
                ],
                'cta_url': '/get-started/?plan=professional',
                'recommended': True
            },
            {
                'name': 'Enterprise',
                'price': 'Custom',
                'period': 'contact sales',
                'features': [
                    'Unlimited employees',
                    'Custom integrations',
                    'Dedicated account manager',
                    'SLA guarantee',
                    'API access'
                ],
                'cta_url': '/contact/',
                'recommended': False
            },
        ]
    }
    return render(request, 'core/for_business.html', context)

# NEW - Careers page view
def careers(request):
    context = {
        'open_positions': [
            {
                'id': 1,
                'title': 'Senior Full Stack Developer',
                'department': 'Engineering',
                'location': 'Remote / Nairobi',
                'type': 'Full-time',
                'experience': '5+ years',
                'description': 'We are looking for an experienced full stack developer to lead our product development efforts. You will work on our core products including the Services Marketplace and Smart Payroll.',
                'responsibilities': [
                    'Design and implement scalable web applications',
                    'Collaborate with product managers and designers',
                    'Write clean, maintainable code',
                    'Mentor junior developers',
                    'Participate in code reviews'
                ],
                'requirements': [
                    '5+ years of experience with Python/Django',
                    'Strong JavaScript/React skills',
                    'Experience with REST APIs and databases',
                    'Excellent problem-solving abilities',
                    'Bachelor\'s degree in Computer Science or equivalent'
                ],
                'apply_url': '/careers/apply/1/'
            },
            {
                'id': 2,
                'title': 'Product Manager',
                'department': 'Product',
                'location': 'Nairobi',
                'type': 'Full-time',
                'experience': '3+ years',
                'description': 'Join our product team to shape the future of SwapLink Integrated. You will drive product strategy, gather requirements, and work closely with engineering.',
                'responsibilities': [
                    'Define product roadmap and strategy',
                    'Gather and prioritize customer requirements',
                    'Work with engineering to deliver features',
                    'Analyze product metrics and user feedback',
                    'Coordinate product launches'
                ],
                'requirements': [
                    '3+ years of product management experience',
                    'Strong understanding of SaaS products',
                    'Excellent communication skills',
                    'Data-driven decision making',
                    'Experience with agile methodologies'
                ],
                'apply_url': '/careers/apply/2/'
            },
            {
                'id': 3,
                'title': 'UI/UX Designer',
                'department': 'Design',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '3+ years',
                'description': 'We need a talented designer to create beautiful, intuitive interfaces for our products. You will shape the user experience across all SwapLink platforms.',
                'responsibilities': [
                    'Create wireframes, prototypes, and high-fidelity designs',
                    'Conduct user research and usability testing',
                    'Collaborate with developers to implement designs',
                    'Maintain design system',
                    'Improve existing product interfaces'
                ],
                'requirements': [
                    '3+ years of UI/UX design experience',
                    'Proficiency with Figma or similar tools',
                    'Strong portfolio demonstrating design work',
                    'Understanding of responsive design',
                    'Experience with design systems'
                ],
                'apply_url': '/careers/apply/3/'
            },
            {
                'id': 4,
                'title': 'Customer Success Manager',
                'department': 'Customer Success',
                'location': 'Nairobi',
                'type': 'Full-time',
                'experience': '2+ years',
                'description': 'Help our customers succeed with SwapLink Integrated. You will onboard new clients, provide support, and ensure customer satisfaction.',
                'responsibilities': [
                    'Onboard new customers and provide training',
                    'Respond to customer inquiries and issues',
                    'Gather customer feedback for product team',
                    'Monitor customer health metrics',
                    'Build strong customer relationships'
                ],
                'requirements': [
                    '2+ years of customer success experience',
                    'Excellent communication and interpersonal skills',
                    'Problem-solving mindset',
                    'Experience with SaaS products',
                    'Bachelor\'s degree preferred'
                ],
                'apply_url': '/careers/apply/4/'
            },
            {
                'id': 5,
                'title': 'Marketing Specialist',
                'department': 'Marketing',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '2+ years',
                'description': 'Drive growth through digital marketing campaigns. You will manage social media, content creation, and lead generation efforts.',
                'responsibilities': [
                    'Develop and execute marketing campaigns',
                    'Manage social media channels',
                    'Create content for blog and email',
                    'Track and report marketing metrics',
                    'Coordinate with sales team'
                ],
                'requirements': [
                    '2+ years of marketing experience',
                    'Experience with social media management',
                    'Strong writing and communication skills',
                    'Analytical mindset',
                    'Familiarity with marketing tools'
                ],
                'apply_url': '/careers/apply/5/'
            },
        ],
        'perks': [
            {'icon': 'fa-globe', 'title': 'Remote First', 'description': 'Work from anywhere. We believe in flexibility and trust.'},
            {'icon': 'fa-chart-line', 'title': 'Growth Opportunities', 'description': 'Continuous learning and career development.'},
            {'icon': 'fa-heart', 'title': 'Health Insurance', 'description': 'Comprehensive health coverage for you and your family.'},
            {'icon': 'fa-clock', 'title': 'Flexible Hours', 'description': 'Focus on results, not hours logged.'},
            {'icon': 'fa-laptop', 'title': 'Equipment Budget', 'description': 'Get the tools you need to do your best work.'},
            {'icon': 'fa-calendar-alt', 'title': 'Paid Time Off', 'description': 'Generous vacation and sick leave policy.'},
        ]
    }
    return render(request, 'core/careers.html', context)

def submit_interest(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(f"New signup: {data}")
            return JsonResponse({'status': 'success', 'message': 'Thank you for your interest!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)