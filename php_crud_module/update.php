<?php
// update.php - Update Existing Project Record via MySQLi Prepared Statement
// Web Technology Lab & Theory Assignment Module
// Student: Md Najmus Sakib Rahatul (ID: 1119003), Dept. of CSE, BAIUST

require_once 'db.php';

$id = isset($_GET['id']) ? (int)$_GET['id'] : 0;
if ($id <= 0) {
    header("Location: index.php");
    exit;
}

// Fetch current project
$stmt = mysqli_prepare($conn, "SELECT * FROM `projects` WHERE `id` = ?");
mysqli_stmt_bind_param($stmt, "i", $id);
mysqli_stmt_execute($stmt);
$res = mysqli_stmt_get_result($stmt);
$project = mysqli_fetch_assoc($res);
mysqli_stmt_close($stmt);

if (!$project) {
    die("Project not found.");
}

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
        $update_stmt = mysqli_prepare($conn, "UPDATE `projects` SET `code`=?, `title`=?, `category`=?, `tech_stack`=?, `summary`=?, `stars_count`=?, `github_url`=? WHERE `id`=?");
        mysqli_stmt_bind_param($update_stmt, "sssssisi", $code, $title, $category, $tech_stack, $summary, $stars_count, $github_url, $id);

        if (mysqli_stmt_execute($update_stmt)) {
            mysqli_stmt_close($update_stmt);
            header("Location: index.php?msg=" . urlencode("Project [$code] updated successfully!"));
            exit;
        } else {
            $error = "Update failed: " . mysqli_error($conn);
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Project | PHP CRUD Module</title>
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
            <span class="text-xs text-slate-500 mono">PHP MySQLi Prepared UPDATE</span>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl">
            <h1 class="text-2xl font-bold text-white mb-2">Edit Project [<?php echo htmlspecialchars($project['code']); ?>]</h1>
            <p class="text-slate-400 text-sm mb-6">Modify records in MySQL table <code>projects</code>.</p>

            <?php if (!empty($error)): ?>
                <div class="mb-6 p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-sm">
                    ✕ <?php echo htmlspecialchars($error); ?>
                </div>
            <?php endif; ?>

            <form action="update.php?id=<?php echo $id; ?>" method="POST" class="space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1 mono">PROJECT CODE *</label>
                        <input type="text" name="code" value="<?php echo htmlspecialchars($project['code']); ?>" required class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500 mono">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">CATEGORY *</label>
                        <select name="category" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500">
                            <option value="Full-Stack Web" <?php echo ($project['category'] === 'Full-Stack Web') ? 'selected' : ''; ?>>Full-Stack Web</option>
                            <option value="IoT & TinyML" <?php echo ($project['category'] === 'IoT & TinyML') ? 'selected' : ''; ?>>IoT & TinyML</option>
                            <option value="Desktop & Systems" <?php echo ($project['category'] === 'Desktop & Systems') ? 'selected' : ''; ?>>Desktop & Systems</option>
                        </select>
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">PROJECT TITLE *</label>
                    <input type="text" name="title" value="<?php echo htmlspecialchars($project['title']); ?>" required class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500">
                </div>

                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">TECH STACK (COMMA-SEPARATED)</label>
                    <input type="text" name="tech_stack" value="<?php echo htmlspecialchars($project['tech_stack']); ?>" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500 mono">
                </div>

                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">SUMMARY / OBJECTIVE *</label>
                    <textarea name="summary" rows="3" required class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500"><?php echo htmlspecialchars($project['summary']); ?></textarea>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">GITHUB REPOSITORY URL</label>
                        <input type="url" name="github_url" value="<?php echo htmlspecialchars($project['github_url']); ?>" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1">STARS COUNT</label>
                        <input type="number" name="stars_count" value="<?php echo (int)$project['stars_count']; ?>" min="0" class="w-full px-4 py-2.5 bg-slate-950 border border-slate-700 rounded-lg text-sm text-white focus:outline-none focus:border-purple-500 mono">
                    </div>
                </div>

                <div class="pt-4 flex items-center justify-end gap-3">
                    <a href="index.php" class="px-5 py-2.5 rounded-lg border border-slate-700 text-slate-300 text-sm hover:bg-slate-800 transition">Cancel</a>
                    <button type="submit" class="px-6 py-2.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-semibold text-sm transition shadow-lg shadow-blue-600/30">Update Project</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
