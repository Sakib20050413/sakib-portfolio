<?php
// create.php - Insert New Project Record via MySQLi Prepared Statement
// Web Technology Lab & Theory Assignment Module
// Student: Md Najmus Sakib Rahatul (ID: 1119003), Dept. of CSE, BAIUST

require_once 'db.php';

$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $code        = trim($_POST['code'] ?? '');
    $title       = trim($_POST['title'] ?? '');
    $category    = trim($_POST['category'] ?? 'Full-Stack Web');
    $tech_stack  = trim($_POST['tech_stack'] ?? '');
    $summary     = trim($_POST['summary'] ?? '');
    $stars_count = (int)($_POST['stars_count'] ?? 0);
    $github_url  = trim($_POST['github_url'] ?? '');

    if (empty($code) || empty($title) || empty($summary)) {
        $error = "Code, Title, and Summary are mandatory fields.";
    } else {
        // Prepared statement to avoid SQL injection
        $stmt = mysqli_prepare($conn, "INSERT INTO `projects` (`code`, `title`, `category`, `tech_stack`, `summary`, `stars_count`, `github_url`) VALUES (?, ?, ?, ?, ?, ?, ?)");
        mysqli_stmt_bind_param($stmt, "sssssis", $code, $title, $category, $tech_stack, $summary, $stars_count, $github_url);
        
        if (mysqli_stmt_execute($stmt)) {
            mysqli_stmt_close($stmt);
            header("Location: index.php?msg=" . urlencode("Project [$code] successfully created in MySQL database!"));
            exit;
        } else {
            $error = "Failed to insert record: " . mysqli_error($conn);
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Project | PHP CRUD Module</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
        .mono { font-family: 'JetBrains Mono', monospace; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen py-10 px-4 md:px-8">
    <div class="max-w-2xl mx-auto">
        <div class="mb-6 flex items-center justify-between">
            <a href="index.php" class="text-sm text-purple-400 hover:text-purple-300 mono">&larr; Back to Master Table</a>
            <span class="text-xs text-slate-500 mono">PHP MySQLi Prepared INSERT</span>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
            <h1 class="text-2xl font-bold text-white mb-2">Create New Portfolio Project</h1>
            <p class="text-slate-400 text-sm mb-6">Insert project data directly into MySQL database table <code>projects</code>.</p>

            <?php if (!empty($error)): ?>
                <div class="mb-6 p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-sm">
                    ✕ <?php echo htmlspecialchars($error); ?>
                </div>
            <?php endif; ?>

            <form action="create.php" method="POST" class="space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1 mono">PROJECT CODE *</label>
                        <input type="text" name="code" placeholder="e.g. A009" required class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500 mono">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">CATEGORY *</label>
                        <select name="category" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500">
                            <option value="Full-Stack Web">Full-Stack Web</option>
                            <option value="IoT & TinyML">IoT & TinyML</option>
                            <option value="Desktop & Systems">Desktop & Systems</option>
                        </select>
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">PROJECT TITLE *</label>
                    <input type="text" name="title" placeholder="e.g. Distributed Task Queue Engine" required class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500">
                </div>

                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">TECH STACK (COMMA-SEPARATED)</label>
                    <input type="text" name="tech_stack" placeholder="e.g. Python, Django, Redis, Docker, Tailwind" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500 mono">
                </div>

                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">SUMMARY / OBJECTIVE *</label>
                    <textarea name="summary" rows="3" placeholder="Brief technical summary of the project..." required class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500"></textarea>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">GITHUB REPOSITORY URL</label>
                        <input type="url" name="github_url" placeholder="https://github.com/Sakib20050413/..." class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">INITIAL STARS</label>
                        <input type="number" name="stars_count" value="0" min="0" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500 mono">
                    </div>
                </div>

                <div class="pt-4 flex items-center justify-end gap-3">
                    <a href="index.php" class="px-5 py-2.5 rounded-lg border border-slate-700 text-slate-300 text-sm hover:bg-slate-800 transition">Cancel</a>
                    <button type="submit" class="px-6 py-2.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white font-semibold text-sm transition shadow-lg shadow-purple-600/30">Save Project Record</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
