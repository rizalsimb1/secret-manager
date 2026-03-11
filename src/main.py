"""CLI entry point using Typer."""
import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from pathlib import Path
import subprocess

app = typer.Typer(
    name="devkit",
    help="🛠  Developer toolkit CLI",
    rich_markup_mode="rich",
    no_args_is_help=True,
)

env_app = typer.Typer(help="Manage environment variables")
app.add_typer(env_app, name="env")
console = Console()


@app.command()
def init(
    name: str = typer.Argument(..., help="Project name"),
    template: str = typer.Option("basic", help="Template to use: basic, fastapi, nextjs"),
    git: bool = typer.Option(True, help="Initialize git repo"),
):
    """Scaffold a new project from a template."""
    rprint(f"[bold green]✨ Creating project:[/bold green] {name} (template: {template})")
    project_dir = Path(name)
    project_dir.mkdir(exist_ok=True)
    (project_dir / "README.md").write_text(f"# {name}\n\nCreated with devkit.\n")
    (project_dir / ".gitignore").write_text("__pycache__/\n*.pyc\n.env\n.venv/\n")
    if git:
        subprocess.run(["git", "init"], cwd=project_dir, capture_output=True)
    rprint(f"[green]✅ Project created:[/green] [bold]{name}/[/bold]")
    rprint(f"[dim]Next:[/dim] cd {name} && devkit run")


@app.command()
def run(
    port: int = typer.Option(8000, help="Port to run on"),
    reload: bool = typer.Option(True, help="Enable auto-reload"),
):
    """Run the development server."""
    rprint(f"[bold blue]🚀 Starting server[/bold blue] on port {port}")
    cmd = ["uvicorn", "app.main:app", f"--port={port}"]
    if reload:
        cmd.append("--reload")
    subprocess.run(cmd)


@env_app.command("list")
def env_list():
    """List all environment variables."""
    env_file = Path(".env")
    if not env_file.exists():
        rprint("[yellow]No .env file found[/yellow]")
        raise typer.Exit()
    table = Table(title=".env variables", show_header=True, header_style="bold cyan")
    table.add_column("Key", style="bold")
    table.add_column("Value", style="dim")
    for line in env_file.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            masked = v[:4] + "***" if len(v) > 4 else "***"
            table.add_row(k.strip(), masked)
    console.print(table)


@env_app.command("set")
def env_set(assignment: str = typer.Argument(..., help="KEY=value")):
    """Set an environment variable in .env."""
    if "=" not in assignment:
        rprint("[red]Error: use KEY=value format[/red]")
        raise typer.Exit(1)
    key, value = assignment.split("=", 1)
    env_file = Path(".env")
    lines = env_file.read_text().splitlines() if env_file.exists() else []
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f"{key}={value}"
            updated = True
            break
    if not updated:
        lines.append(f"{key}={value}")
    env_file.write_text("\n".join(lines) + "\n")
    rprint(f"[green]✓[/green] Set [bold]{key}[/bold]")


if __name__ == "__main__":
    app()
