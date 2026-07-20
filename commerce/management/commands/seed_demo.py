from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils import timezone

from blog.models import Category, Post, Tag
from commerce.models import (
    JobOpening,
    MentorshipCohort,
    OutreachEvent,
    Partner,
    PricingPlan,
    Product,
    Project,
    Service,
    TeamMember,
    Testimonial,
)


class Command(BaseCommand):
    help = "Create WWT demo content for the platform."

    def handle(self, *args, **options):
        user_model = get_user_model()
        user, _ = user_model.objects.get_or_create(
            username="editor",
            defaults={"email": "editor@example.com", "is_staff": True, "is_superuser": True},
        )
        if not user.has_usable_password():
            user.set_password("ChangeMe123!")
            user.save(update_fields=["password"])

        Service.objects.filter(slug__isnull=True).update(is_active=False)

        services = [
            (
                "DevOps Systems",
                "technology",
                "Cloud infrastructure, automation, CI/CD pipelines, monitoring, Kubernetes, Docker, infrastructure as code, security, and deployment optimization.",
                "Kubernetes\nDocker\nLinux\nTerraform\nGitHub Actions\nPrometheus\nGrafana",
                "Government\nFinancial services\nStartups\nUniversities",
                "Faster releases\nImproved reliability\nBetter observability\nLower deployment risk",
                "bi-diagram-3",
            ),
            (
                "PV Systems",
                "energy",
                "Solar design, installation, monitoring, energy audits, hybrid systems, and commercial or residential solar solutions.",
                "PVsyst\nSolarEdge\nVictron\nHybrid inverters\nBattery storage",
                "Homes\nSchools\nHealthcare\nSMEs\nRural communities",
                "Reduced energy cost\nImproved resilience\nCleaner power\nBetter monitoring",
                "bi-sun",
            ),
            (
                "IoT Systems",
                "technology",
                "Smart agriculture, smart buildings, remote monitoring, industrial automation, sensor networks, and embedded systems.",
                "MQTT\nESP32\nRaspberry Pi\nLoRaWAN\nPython\nPostgreSQL",
                "Agriculture\nEnergy\nBuildings\nManufacturing",
                "Remote visibility\nAutomation\nPredictive maintenance\nData-driven decisions",
                "bi-broadcast-pin",
            ),
            (
                "Software Development",
                "technology",
                "Custom software, mobile apps, web platforms, APIs, and enterprise systems for public and private institutions.",
                "Python\nDjango\nPostgreSQL\nREST APIs\nBootstrap\nJavaScript",
                "Public sector\nSMEs\nEducation\nEnergy\nResearch",
                "Secure platforms\nAdmin-managed content\nIntegrated workflows\nScalable architecture",
                "bi-code-slash",
            ),
            (
                "Strategic Design",
                "design",
                "Design thinking, human-centered innovation, organizational strategy, digital transformation, and policy design.",
                "Systems thinking\nService design\nResearch synthesis\nWorkshop facilitation",
                "Government\nNGOs\nEnterprises\nUniversities",
                "Clear strategy\nBetter services\nAligned teams\nEvidence-led decisions",
                "bi-bezier2",
            ),
            (
                "Green Energy Advocacy",
                "advocacy",
                "Research, policy, training, renewable adoption, and community education for sustainable energy transitions.",
                "Policy research\nTraining\nCommunity education\nEnergy audits",
                "Communities\nSchools\nCounty governments\nCivil society",
                "Public awareness\nRenewable adoption\nCapacity building\nBetter policy dialogue",
                "bi-megaphone",
            ),
        ]
        for order, (title, area, summary, technologies, industries, benefits, icon) in enumerate(services, 1):
            Service.objects.update_or_create(
                slug=slugify(title),
                defaults={
                    "title": title,
                    "area": area,
                    "summary": summary,
                    "description": summary,
                    "technologies": technologies,
                    "industries": industries,
                    "benefits": benefits,
                    "icon": icon,
                    "order": order,
                    "is_active": True,
                },
            )

        Product.objects.get_or_create(
            slug="starter-website",
            defaults={
                "name": "Starter Website",
                "description": "A responsive business website package with core pages and admin-managed content.",
                "price": 950,
                "is_featured": True,
            },
        )
        Product.objects.get_or_create(
            slug="content-engine",
            defaults={
                "name": "Content Engine",
                "description": "Blog, search, categories, RSS, newsletter, and publishing workflows.",
                "price": 1450,
                "is_featured": True,
            },
        )

        plans = [
            ("Discovery", "Consulting", "Strategic assessment for software, energy, or institutional design work.", "Research\nTechnical audit\nRoadmap\nExecutive brief", False),
            ("Build", "Project", "Implementation of resilient platforms, solar systems, IoT deployments, or design programs.", "Architecture\nDelivery\nDocumentation\nTraining", True),
            ("Operate", "Retainer", "Ongoing engineering, monitoring, optimization, and advisory support.", "DevOps support\nSystem monitoring\nContent operations\nContinuous improvement", False),
        ]
        for order, (name, price, description, features, featured) in enumerate(plans, 1):
            PricingPlan.objects.update_or_create(
                name=name,
                defaults={"price": price, "description": description, "features": features, "is_featured": featured, "order": order},
            )

        Project.objects.update_or_create(
            slug="solar-monitoring-pilot",
            defaults={
                "title": "Solar Monitoring Pilot",
                "project_type": "solar",
                "summary": "A PV monitoring concept for tracking generation, battery health, and load behavior.",
                "description": "A demonstration project connecting solar system data to dashboards for better energy decisions.",
                "location": "Kenya",
                "year": timezone.now().year,
                "technologies": "PV Systems\nIoT Sensors\nPython\nDashboards",
                "outcome": "Improved visibility into renewable energy performance.",
                "is_featured": True,
                "is_published": True,
            },
        )
        Project.objects.update_or_create(
            slug="django-knowledge-hub",
            defaults={
                "title": "Django Knowledge Hub",
                "project_type": "software",
                "summary": "A publishing, recruitment, outreach, and mentorship platform for a corporate knowledge hub.",
                "description": "A Django platform with admin-managed content, newsletter updates, forms, and searchable articles.",
                "location": "Remote",
                "year": timezone.now().year,
                "technologies": "Python\nDjango\nSQLite\nBootstrap\nEmail",
                "outcome": "One digital platform for corporate communication and community engagement.",
                "is_featured": True,
                "is_published": True,
            },
        )

        JobOpening.objects.update_or_create(
            slug="senior-devops-engineer",
            defaults={
                "title": "Senior DevOps Engineer",
                "location": "Nairobi",
                "employment_type": "full_time",
                "summary": "Lead cloud infrastructure, automation, deployment pipelines, and observability for WWT systems.",
                "responsibilities": "Design CI/CD pipelines\nManage Linux and cloud infrastructure\nImprove monitoring and incident response\nDocument operational standards",
                "requirements": "Strong Linux experience\nDocker and Kubernetes experience\nInfrastructure as code knowledge\nPython scripting ability",
                "is_active": True,
            },
        )
        JobOpening.objects.update_or_create(
            slug="solar-engineer",
            defaults={
                "title": "Solar Engineer",
                "location": "Kenya",
                "employment_type": "contract",
                "summary": "Support PV system design, audits, installation supervision, monitoring, and client documentation.",
                "responsibilities": "Conduct energy audits\nPrepare PV designs\nCoordinate installations\nTrain clients on monitoring",
                "requirements": "PV design experience\nKnowledge of inverters and battery systems\nField documentation skills\nSafety-first mindset",
                "is_active": True,
            },
        )

        OutreachEvent.objects.update_or_create(
            slug="university-stem-outreach",
            defaults={
                "title": "University STEM Outreach",
                "program_type": "University Partnerships",
                "summary": "A program connecting students with practical software, DevOps, IoT, and renewable energy learning.",
                "description": "WWT partners with universities to offer talks, practical labs, project critique, and career guidance.",
                "location": "Nairobi",
                "is_published": True,
            },
        )

        MentorshipCohort.objects.update_or_create(
            slug="software-engineering-mentorship",
            defaults={
                "title": "Software Engineering Mentorship",
                "track": "software",
                "summary": "Python, Django, DevOps, cloud, Linux, and backend development mentorship.",
                "description": "A cohort for learners building practical backend and infrastructure skills.",
                "is_open": True,
            },
        )

        TeamMember.objects.update_or_create(
            name="WWT Leadership",
            defaults={
                "role": "Technology, Energy and Strategy",
                "bio": "A multidisciplinary leadership team focused on resilient engineering, sustainable energy, and African institutional transformation.",
                "order": 1,
                "is_active": True,
            },
        )
        Partner.objects.update_or_create(
            name="Open Source Community",
            defaults={"description": "Collaborating through open tools, knowledge sharing, and practical engineering education.", "is_active": True},
        )

        Testimonial.objects.update_or_create(
            name="Amina Patel",
            defaults={"role": "Founder", "quote": "WWT brings engineering discipline, energy awareness, and strategy into one practical platform."},
        )

        categories = [
            ("systems-engineering-design", "Systems Engineering & Design"),
            ("strategic-design", "Strategic Design"),
            ("tta-project", "TTA Project"),
        ]
        for category_slug, category_name in categories:
            Category.objects.get_or_create(slug=category_slug, defaults={"name": category_name})
        category = Category.objects.get(slug="systems-engineering-design")
        tag, _ = Tag.objects.get_or_create(slug="devops", defaults={"name": "DevOps"})
        Post.objects.update_or_create(
            slug="elevating-africa-through-resilient-systems",
            defaults={
                "title": "Elevating Africa Through Resilient Systems",
                "author": user,
                "category": category,
                "summary": "Why software engineering, sustainable energy, and strategic design belong in the same African transformation agenda.",
                "content": "Africa needs resilient systems across technology, energy, public administration, and enterprise operations.\n\nWWT approaches this through software engineering, PV systems, IoT, DevOps, strategic design, and advocacy. The objective is not only digital adoption, but technological independence and institutional capacity.",
                "published": True,
                "published_at": timezone.now(),
            },
        )[0].tags.add(tag)
        self.stdout.write(self.style.SUCCESS("Demo content created. Admin user: editor / ChangeMe123!"))
