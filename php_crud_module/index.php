<?php
// index.php - Procedural PHP + MySQLi CRUD Dashboard
// Web Technology Lab & Theory Assignment Module
// Student: Md Najmus Sakib Rahatul (ID: 1119003), Dept. of CSE, BAIUST

require_once 'db.php';

// Fetch projects
$search = isset($_GET['search']) ? mysqli_real_escape_string($conn, $_GET['search']) : '';
if (!empty($search)) {
    $projects_sql = "SELECT * FROM `projects` WHERE `title` LIKE '%$search%' OR `code` LIKE '%$search%' OR `category` LIKE '%$search%' ORDER BY `id` DESC";
} else {
    $projects_sql = "SELECT * FROM `projects` ORDER BY `id` DESC";
}
$projects_result = mysqli_query($conn, $projects_sql);

// Fetch messages
$messages_sql = "SELECT * FROM `messages` ORDER BY `id` DESC";
$messages_result = mysqli_query($conn, $messages_sql);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP + MySQLi CRUD Module | Md Najmus Sakib Rahatul (1119003)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
        .mono { font-family: 'JetBrains Mono', monospace; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen py-10 px-4 md:px-8">

    <div class="max-w-6xl mx-auto">
        <!-- Academic Header -->
        <header class="border-b border-slate-800 pb-6 mb-8 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div>
                <div class="flex items-center gap-3">
                    <span class="px-2.5 py-1 text-xs rounded-md bg-purple-500/20 text-purple-300 border border-purple-500/30 mono font-semibold">CSE 323 / 324 LAB MODULE</span>
                    <span class="text-xs text-slate-400">PHP 8.x + MySQLi Procedural CRUD</span>
                </div>
                <h1 class="text-3xl font-bold text-white mt-2">Portfolio Management PHP CRUD Bridge</h1>
                <p class="text-slate-400 text-sm mt-1">Student: <strong class="text-purple-300">Md Najmus Sakib Rahatul</strong> (ID: <code>1119003</code>) • Level 3 Term 2 • BAIUST</p>
            </div>
            <div class="flex items-center gap-3">
                <a href="http://127.0.0.1:8000" target="_blank" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-sm font-medium rounded-lg transition border border-slate-700 flex items-center gap-2">
                    <span>⚡ Return to Django Portfolio</span>
                </a>
                <a href="create.php" class="px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-sm font-semibold rounded-lg shadow-lg shadow-purple-600/30 transition flex items-center gap-1.5">
                    <span>+ Add New Project</span>
                </a>
            </div>
        </header>

        <!-- Flash Notice / Feedback -->
        <?php if (isset($_GET['msg'])): ?>
            <div class="mb-6 p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-sm flex items-center justify-between">
                <span>✓ <?php echo htmlspecialchars($_GET['msg']); ?></span>
                <a href="index.php" class="text-emerald-400 hover:text-emerald-200 font-bold ml-4">✕</a>
            </div>
        <?php endif; ?>

        <!-- Search Bar -->
        <div class="mb-6 flex flex-col sm:flex-row gap-4 items-center justify-between bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <form action="index.php" method="GET" class="flex-1 w-full flex gap-2">
                <input type="text" name="search" value="<?php echo htmlspecialchars($search); ?>" placeholder="Search projects by code (A001), title, or category..." class="w-full px-4 py-2 bg-slate-950 border border-slate-700 rounded-lg text-sm text-slate-200 focus:outline-none focus:border-purple-500">
                <button type="submit" class="px-5 py-2 bg-slate-800 hover:bg-slate-700 text-white text-sm font-medium rounded-lg transition border border-slate-700">Filter</button>
                <?php if (!empty($search)): ?>
                    <a href="index.php" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-slate-200 text-sm rounded-lg border border-slate-700 flex items-center">Reset</a>
                <?php endif; ?>
            </form>
            <div class="text-xs text-slate-400 mono">
                Total Projects: <strong class="text-purple-400"><?php echo mysqli_num_rows($projects_result); ?></strong>
            </div>
        </div>

        <!-- Section 1: Projects Table -->
        <section class="mb-12">
            <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
                <span>📁</span> Project Database (CRUD Master Table)
            </h2>
            <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/40">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="bg-slate-900/80 text-xs uppercase text-slate-400 border-b border-slate-800 mono">
                        <tr>
                            <th class="px-4 py-3.5">Code</th>
                            <th class="px-4 py-3.5">Title & Summary</th>
                            <th class="px-4 py-3.5">Category</th>
                            <th class="px-4 py-3.5">Tech Stack</th>
                            <th class="px-4 py-3.5 text-center">Stars</th>
                            <th class="px-4 py-3.5 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60">
                        <?php if (mysqli_num_rows($projects_result) > 0): ?>
                            <?php while ($proj = mysqli_fetch_assoc($projects_result)): ?>
                                <tr class="hover:bg-slate-800/30 transition">
                                    <td class="px-4 py-4 font-mono font-semibold text-purple-400">
                                        <?php echo htmlspecialchars($proj['code']); ?>
                                    </td>
                                    <td class="px-4 py-4 max-w-sm">
                                        <div class="font-bold text-slate-100 text-base"><?php echo htmlspecialchars($proj['title']); ?></div>
                                        <div class="text-xs text-slate-400 mt-1 line-clamp-2"><?php echo htmlspecialchars($proj['summary']); ?></div>
                                        <?php if (!empty($proj['github_url'])): ?>
                                            <a href="<?php echo htmlspecialchars($proj['github_url']); ?>" target="_blank" class="inline-block mt-1 text-xs text-indigo-400 hover:underline">Repo Link &rarr;</a>
                                        <?php endif; ?>
                                    </td>
                                    <td class="px-4 py-4">
                                        <span class="px-2.5 py-1 text-xs font-medium rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                                            <?php echo htmlspecialchars($proj['category']); ?>
                                        </span>
                                    </td>
                                    <td class="px-4 py-4 text-xs font-mono text-slate-300 max-w-xs">
                                        <?php echo htmlspecialchars($proj['tech_stack']); ?>
                                    </td>
                                    <td class="px-4 py-4 text-center font-mono text-amber-400 font-semibold">
                                        ★ <?php echo (int)$proj['stars_count']; ?>
                                    </td>
                                    <td class="px-4 py-4 text-right space-x-2">
                                        <a href="update.php?id=<?php echo $proj['id']; ?>" class="px-3 py-1.5 bg-blue-600/20 hover:bg-blue-600/40 text-blue-300 border border-blue-500/30 rounded-lg text-xs font-medium transition inline-block">
                                            Edit
                                        </a>
                                        <a href="delete.php?type=project&id=<?php echo $proj['id']; ?>" onclick="return confirm('Are you sure you want to delete project [<?php echo htmlspecialchars($proj['code']); ?>]?');" class="px-3 py-1.5 bg-rose-600/20 hover:bg-rose-600/40 text-rose-300 border border-rose-500/30 rounded-lg text-xs font-medium transition inline-block">
                                            Delete
                                        </a>
                                    </td>
                                </tr>
                            <?php endwhile; ?>
                        <?php else: ?>
                            <tr>
                                <td colspan="6" class="px-4 py-8 text-center text-slate-500">
                                    No projects found in MySQL database matching criteria.
                                </td>
                            </tr>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Section 2: Contact Messages Table -->
        <section>
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-xl font-bold text-white flex items-center gap-2">
                    <span>💬</span> Incoming Messages (PHP Table)
                </h2>
                <span class="text-xs text-slate-400 mono">Total Messages: <?php echo mysqli_num_rows($messages_result); ?></span>
            </div>
            <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/40">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="bg-slate-900/80 text-xs uppercase text-slate-400 border-b border-slate-800 mono">
                        <tr>
                            <th class="px-4 py-3.5">Sender</th>
                            <th class="px-4 py-3.5">Email</th>
                            <th class="px-4 py-3.5">Subject</th>
                            <th class="px-4 py-3.5">Message Content</th>
                            <th class="px-4 py-3.5">Received Date</th>
                            <th class="px-4 py-3.5 text-right">Action</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60">
                        <?php if (mysqli_num_rows($messages_result) > 0): ?>
                            <?php while ($msg = mysqli_fetch_assoc($messages_result)): ?>
                                <tr class="hover:bg-slate-800/30 transition">
                                    <td class="px-4 py-4 font-semibold text-slate-200"><?php echo htmlspecialchars($msg['sender_name']); ?></td>
                                    <td class="px-4 py-4 font-mono text-xs text-purple-300"><?php echo htmlspecialchars($msg['sender_email']); ?></td>
                                    <td class="px-4 py-4 font-medium text-slate-200"><?php echo htmlspecialchars($msg['subject']); ?></td>
                                    <td class="px-4 py-4 text-xs text-slate-400 max-w-sm"><?php echo htmlspecialchars($msg['message']); ?></td>
                                    <td class="px-4 py-4 text-xs text-slate-500 font-mono"><?php echo htmlspecialchars($msg['created_at']); ?></td>
                                    <td class="px-4 py-4 text-right">
                                        <a href="delete.php?type=message&id=<?php echo $msg['id']; ?>" onclick="return confirm('Delete message from <?php echo htmlspecialchars($msg['sender_name']); ?>?');" class="text-xs text-rose-400 hover:text-rose-300">
                                            Delete
                                        </a>
                                    </td>
                                </tr>
                            <?php endwhile; ?>
                        <?php else: ?>
                            <tr>
                                <td colspan="6" class="px-4 py-8 text-center text-slate-500">No contact messages logged yet.</td>
                            </tr>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Footer -->
        <footer class="mt-12 pt-6 border-t border-slate-800 text-center text-xs text-slate-500 mono">
            Web Technology Assignment Module • Dept. of CSE, BAIUST, Cumilla • PHP Procedural + MySQLi API
        </footer>
    </div>

</body>
</html>
