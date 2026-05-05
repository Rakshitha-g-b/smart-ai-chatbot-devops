def get_ai_reply(message: str) -> str:
    text = message.lower().strip()

    if "career" in text:
        return "To build a strong career, improve coding skills, make projects, practice interviews, and maintain a good GitHub profile."
    elif "docker" in text:
        return "Docker is a tool that packages your application and its dependencies into a container so it runs the same everywhere."
    elif "kubernetes" in text:
        return "Kubernetes is a container orchestration platform that helps deploy, manage, and scale applications automatically."
    elif "github actions" in text:
        return "GitHub Actions is used to automate tasks like testing, building, and deployment whenever code is pushed."
    elif "devops" in text:
        return "DevOps is a practice that combines development and operations to automate software delivery and monitoring."
    elif "prometheus" in text:
        return "Prometheus collects metrics such as request counts, uptime, and response times for monitoring."
    elif "grafana" in text:
        return "Grafana visualizes monitoring data from Prometheus using dashboards and graphs."
    else:
        return f"You asked: '{message}'. For the full AI version, connect this chatbot to an LLM API like OpenRouter or Perplexity API."